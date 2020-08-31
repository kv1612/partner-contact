# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _create_delivery_line(self, carrier, price_unit):
        line = super()._create_delivery_line(carrier, price_unit)
        product = carrier.product_id
        if self.partner_id:
            product = product.with_context(lang=self.partner_id.lang)
        # We only want to display the product name (currently: "Additional
        # Fees") in the line, in the customer's language. Since free lines
        # (module delivery_free_fee_removal) are removed, we don't care about
        # the "Free Shipping" mention of the original "delivery" module.
        line.name = product.name
        return line
