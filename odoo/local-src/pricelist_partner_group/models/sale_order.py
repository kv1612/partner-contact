# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models
from odoo.tools import float_is_zero


class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        # The super call already sets the pricelist from the partner.
        result = super().onchange_partner_id()
        if self.partner_id and self.partner_id.partner_group_pricelist_id:
            self.pricelist_id = self.partner_id.partner_group_pricelist_id
        return result

    def _product_ids_with_fixed_prices(self, pricelists):
        order_products = self.order_line.mapped("product_id")
        product_ids = []
        today = fields.Date.today()
        query = """
            SELECT product_id
            FROM product_pricelist_item
            WHERE compute_price = 'fixed'
                AND pricelist_id in %(pricelist_ids)s
                AND product_id IN %(product_ids)s
                AND applied_on = '0_product_variant'
                AND active = TRUE
                AND (date_start IS NULL or date_start <= %(today)s)
                AND (date_end IS NULL or date_end >= %(today)s)
            UNION
            SELECT pp.id
            FROM product_product pp
            JOIN product_pricelist_item ppi
                ON pp.product_tmpl_id = ppi.product_tmpl_id
            WHERE ppi.compute_price = 'fixed'
                AND ppi.pricelist_id in %(pricelist_ids)s
                AND ppi.product_tmpl_id IN %(template_ids)s
                AND ppi.applied_on = '1_product'
                AND ppi.active = TRUE
                AND (ppi.date_start IS NULL OR ppi.date_start <= %(today)s)
                AND (ppi.date_end IS NULL OR ppi.date_end >= %(today)s);
        """
        args = {
            "pricelist_ids": tuple(pricelists.ids),
            "product_ids": tuple(order_products.ids),
            "template_ids": tuple(
                order_products.mapped("product_tmpl_id").ids
            ),
            "today": today,
        }
        self.env.cr.execute(query, args)
        res = self.env.cr.fetchall()
        product_ids = [row[0] for row in res]
        return product_ids

    def action_confirm(self):
        """Handle pricelist based on industry.

        If partner's industry in one of the industries specified in the config
        and if ordered products are ordered for the first time then the
        price is saved on its group (if any) or user pricelist for future orders.
        """
        res = super().action_confirm()
        industries = self.env.user.company_id.pricelist_industry_ids
        pricelist_item_vals = []
        for order in self:
            seen_products = []
            company = order.partner_id.commercial_partner_id
            # Company not in specified industries
            if company.industry_id not in industries:
                continue
            partner_pricelist = company.property_product_pricelist
            group_pricelist = (
                company.company_group_id.property_product_pricelist
            )
            product_ids_in_pricelist = order._product_ids_with_fixed_prices(
                group_pricelist | partner_pricelist
            )
            for line in order.order_line:
                # Since the golive, there's grey lines on sale orders which don't
                # have a product_id. We do not want those lines to trigger
                # the creation of pricelist items
                product_id = line.product_id.id
                if line.display_type or product_id in product_ids_in_pricelist:
                    continue
                # Do not store the price if it is 0.0
                if float_is_zero(
                    line.price_unit,
                    precision_rounding=order.currency_id.rounding,
                ):
                    continue
                # We do not want to create multiple pricelist items for a single
                # product
                if product_id in seen_products:
                    continue
                seen_products.append(product_id)
                # No fixed price for product, create a new one
                pricelist_item_vals.append(
                    {
                        "applied_on": "0_product_variant",
                        "compute_price": "fixed",
                        "fixed_price": line.price_unit,
                        "product_id": product_id,
                        "pricelist_id": group_pricelist.id
                        or partner_pricelist.id,
                    }
                )
        self.env["product.pricelist.item"].create(pricelist_item_vals)
        return res
