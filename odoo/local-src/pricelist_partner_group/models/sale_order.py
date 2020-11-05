# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        # The super call already sets the pricelist from the partner.
        result = super().onchange_partner_id()
        if self.partner_id and self.partner_id.partner_group_pricelist_id:
            self.pricelist_id = self.partner_id.partner_group_pricelist_id
        return result

    @staticmethod
    def _pricelist_fixed_price_lines_by_product(pricelist):
        """Return mapping of pricelist lines by product."""
        return {
            line.product_id.id: line
            for line in pricelist.item_ids
            if line.compute_price == "fixed"
        }

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
            company = order.partner_id.commercial_partner_id
            # Company not in specified industries
            if company.industry_id not in industries:
                continue
            partner_pricelist = company.property_product_pricelist
            group_pricelist = (
                company.company_group_id.property_product_pricelist
            )
            partner_pricelist_lines_by_product = self._pricelist_fixed_price_lines_by_product(
                partner_pricelist
            )
            group_pricelist_lines_by_product = self._pricelist_fixed_price_lines_by_product(
                group_pricelist
            )
            for line in order.order_line:
                partner_fixed_price = partner_pricelist_lines_by_product.get(
                    line.product_id.id
                )
                group_fixed_price = group_pricelist_lines_by_product.get(
                    line.product_id.id
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
