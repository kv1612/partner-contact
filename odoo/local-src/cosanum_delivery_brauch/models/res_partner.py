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
        "mobile",
        "phone",
    )
    def _compute_brauch_delivery_info(self):
        desc = self.with_context(lang="de_DE").get_delivery_time_description()
        for partner in self:
            delivery_times_string = _("Delivery times:\n%s") % desc.get(
                partner.id
            )
            delivery_phone_string = ""
            delivery_mobile_string = ""
            if partner.phone:
                delivery_phone_string = _("Phone number: %s") % partner.phone
            if partner.mobile:
                delivery_mobile_string = (
                    _("Mobile number: %s") % partner.mobile
                )
            partner.brauch_delivery_info = "\n".join(
                [
                    delivery_times_string,
                    delivery_phone_string,
                    delivery_mobile_string,
                ]
            )
