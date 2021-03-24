# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
import ftplib
from io import BytesIO

from odoo import _, exceptions, fields, models
from odoo.addons.queue_job.job import job


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(
        selection_add=[('brauch', "Brauch Transporte")]
    )
    brauch_default_packaging_id = fields.Many2one(
        "product.packaging",
        domain=[("package_carrier_type", "=", "brauch")],
        string="Default Packaging",
    )
    brauch_ftp_uri = fields.Char()
    brauch_ftp_path = fields.Char()
    brauch_ftp_login = fields.Char()
    brauch_ftp_password = fields.Char()
    brauch_datetime_format = fields.Char(default="%d.%m.%Y %H:%M")
    brauch_filename = fields.Char(
        default="'%s_%s_%s.csv' % (object.company_id.name, object.partner_id.name or '', object.name)",
        help="This is the filename of the csv file to download. You can use a "
        "python expression with the 'object' and 'time' variables.",
    )

    def brauch_rate_shipment(self, order):
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
        return {
            "success": True,
            "price": 0.0,
            "error_message": False,
            "warning_message": False,
        }

    def brauch_get_tracking_link(self, picking):
        return False

    def brauch_cancel_shipment(self, pickings):
        raise NotImplementedError()

    def brauch_send_shipping(self, pickings):
        res = []
        for pick in pickings:
            res.append(pick._send_delivery_to_brauch())
        return res

    @job
    def _brauch_push_to_ftp(self, csv_data, csv_file_name):
        if not (
            self.brauch_ftp_uri
            and self.brauch_ftp_login
            and self.brauch_ftp_password
        ):
            raise exceptions.UserError(_("Missing credentials for FTP"))
        with ftplib.FTP(
            self.brauch_ftp_uri,
            self.brauch_ftp_login,
            self.brauch_ftp_password,
        ) as ftp:
            if self.brauch_ftp_path:
                ftp.cwd(self.brauch_ftp_path)
            with BytesIO() as file_obj:
                file_obj.write(csv_data.encode())
                file_obj.seek(0)
                ftp.storbinary("STOR %s" % csv_file_name, file_obj)

    def _brauch_get_csv_columns(self):
        return [
            "Ist-Anz. Pal.",
            "K-PID",
            "Gewicht (kg)",
            "Verladedatum",
            "Auftrags-Prio",
            "Lieferdatum",
            "Lieferschein-Nr",
            "Tour",
            "Lieferant-PLZ",
            "Lieferant-Ort",
            "Lieferant-Name",
            "Lieferant-Zusatz Name",
            "Lieferant-Adres Zusatz",
            "Lieferant-Strasse",
            "Auslieferhinweis (Info 2)",
        ]
