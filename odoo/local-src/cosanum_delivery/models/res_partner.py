# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    truck_weight_limit = fields.Selection(
        selection="_selection_truck_weight_limit",
        string="Truck Weight limit (in T)",
    )
    delivery_info = fields.Text(string="Info for delivery carrier")

    @api.model
    def _selection_truck_weight_limit(self):
        return [("3.5", "3.5"), ("18", "18"), ("40", "40")]
