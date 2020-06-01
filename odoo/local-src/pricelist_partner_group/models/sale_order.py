# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    @classmethod
    def _get_pricelist_line(cls, pricelist, product):
        item_ids = pricelist.item_ids.filtered(
            lambda i: i.product_id.id == product.id
            and i.compute_price == "fixed"
        )
        return item_ids

    def action_confirm(self):
        """
        If partner's industry in one of the industries specified in the config
        and if ordered products are ordered for the first time then the
        price is saved on its group (if any) or user pricelist for future orders.
        """
        res = super().action_confirm()
        industries = self.env.user.company_id.pricelist_industry_ids
        pricelist_item_vals = []
        for order in self:
            company = order.partner_id.commercial_partner_id
            # Company not in specified industries
            if company.industry_id not in industries:
                continue
            partner_pricelist = company.property_product_pricelist
            group_pricelist = (
                company.company_group_id.property_product_pricelist
            )
            for line in order.order_line:
                partner_fixed_price = self._get_pricelist_line(
                    partner_pricelist, line.product_id
                )
                group_fixed_price = self._get_pricelist_line(
                    group_pricelist, line.product_id
                )
                if partner_fixed_price or group_fixed_price:
                    continue
                # No fixed price for product, create a new one
                pricelist_item_vals.append(
                    {
                        "applied_on": "0_product_variant",
                        "compute_price": "fixed",
                        "fixed_price": line.price_unit,
                        "product_id": line.product_id.id,
                        "pricelist_id": group_pricelist.id
                        or partner_pricelist.id,
                    }
                )
        self.env["product.pricelist.item"].create(pricelist_item_vals)
        return res
