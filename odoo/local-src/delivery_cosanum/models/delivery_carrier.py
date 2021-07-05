# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, fields, models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    delivery_type = fields.Selection(selection_add=[("cosanum", "Cosanum")])
    cosanum_default_packaging_id = fields.Many2one(
        "product.packaging",
        domain=[("package_carrier_type", "=", "cosanum")],
        string="Cosanum Default Packaging",
    )

    def cosanum_rate_shipment(self, order):
        self.ensure_one()
        carrier = self._match_address(order.partner_shipping_id)
        if not carrier:
            return {
                "success": False,
                "price": 0.0,
                "error_message": _(
                    "Error: this delivery method is not available for this address."
                ),
                "warning_message": False,
            }
        delivery_product_price = (
            self.product_id and self.product_id.lst_price or 0
        )
        return {
            "success": True,
            "price": delivery_product_price,
            "error_message": False,
            "warning_message": False,
        }

    def cosanum_send_shipping(self, pickings):
        return [
            {'exact_price': 0.0, 'tracking_number': False} for p in pickings
        ]
