# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    brauch_delivery_info = fields.Text(compute="_compute_brauch_delivery_info")

    @api.depends(
        "delivery_time_preference",
        "delivery_time_window_ids.time_window_weekday_ids",
        "delivery_time_window_ids.time_window_start",
        "delivery_time_window_ids.time_window_end",
        "delivery_info_id",
        "delivery_info_id.text",
    )
    def _compute_brauch_delivery_info(self):
        desc = self.with_context(lang="de_DE").get_delivery_time_description()
        for partner in self:
            delivery_times_string = _("Anytime")
            if partner.delivery_time_preference == "time_windows":
                delivery_times_string = desc.get(partner.id)
            partner.brauch_delivery_info = delivery_times_string

    def _get_delivery_time_format_string(self):
        # Override the method of 'stock_partner_delivery_window'
        return "%s - %s"
