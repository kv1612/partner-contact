# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class DeliveryCarrier(models.Model):
    _name = "delivery.carrier"
    _inherit = ["delivery.carrier", "server.env.mixin"]

    def _brauch_get_csv_columns(self):
        res = super()._brauch_get_csv_columns()
        res.append("Schlieren")
        res.append("Werrikon")
        return res

    def _brauch_get_common_picking_data(self):
        res = super()._brauch_get_common_picking_data()
        if self.partner_id.delivery_time_preference == "time_windows":
            res["Auftrags-Prio"] = "Fixtermin"
        return res

    @property
    def _server_env_fields(self):
        base_fields = super()._server_env_fields
        brauch_fields = {
            "brauch_ftp_uri": {},
            "brauch_ftp_path": {},
            "brauch_ftp_login": {},
            "brauch_ftp_password": {},
        }
        brauch_fields.update(base_fields)
        return brauch_fields

    def _server_env_section_name(self):
        """Name of the section in the configuration files

        Can be customized in your model
        """
        self.ensure_one()
        base = self._server_env_global_section_name()
        if self.delivery_type == "brauch":

            return ".".join((base, "brauch"))
        else:
            return super()._server_env_section_name()
