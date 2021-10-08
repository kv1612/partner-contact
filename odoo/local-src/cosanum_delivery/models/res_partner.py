# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    truck_weight_limit = fields.Selection(
        selection="_selection_truck_weight_limit",
        string="Truck Weight limit (in T)",
    )
    delivery_notifications_phone = fields.Char(
        string="Phone for Delivery Carrier Notifications"
    )
    customs_privileged = fields.Selection(
        selection=[("gdk", "GDK"), ("no_gdk", "No GDK")],
        string="Customs privileged",
    )
    # Change default value
    # Field coming from `sale_partner_delivery_window`
    # TODO: to enable once the addon is migrated (check `sale_delivery_dates`?)
    # delivery_time_preference = fields.Selection(default="workdays")

    @api.model
    def _selection_truck_weight_limit(self):
        return [("3.5", "3.5"), ("18", "18"), ("40", "40")]
