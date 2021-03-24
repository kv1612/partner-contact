# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    delivery_type = fields.Selection(selection_add=[("cosanum", "Cosanum")])
    cosanum_default_packaging_id = fields.Many2one(
        "product.packaging", string="Default Packaging"
    )
