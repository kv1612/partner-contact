# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
import base64
import csv
import time
from io import StringIO

from odoo import _, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class StockPicking(models.Model):

    _inherit = "stock.picking"

    brauch_exported_file = fields.Binary(attachment=True, readonly=True)
    brauch_exported_filename = fields.Char()
    brauch_exported_file_display = fields.Boolean(
        compute="_compute_brauch_exported_file_display"
    )

    def _brauch_get_carrier(self):
        self.ensure_one()
        return self.carrier_id

    def _compute_brauch_exported_file_display(self):
        for pick in self:
            pick.brauch_exported_file_display = (
                pick.state == "done"
                and (pick._brauch_get_carrier().delivery_type == "brauch")
                and pick.brauch_exported_file
            )

    def _send_delivery_to_brauch(self):
        csv_data = self._generate_brauch_csv()
        # Do not send the csv if it just contains the header
        # Check for empty lines, since a "\n" is automatically appended on
        # the header.
        csv_lines = [line for line in csv_data.split("\n", 2) if line.strip()]
        if len(csv_lines) > 1:
            csv_file_name = safe_eval(
                self.carrier_id.brauch_filename, {"object": self, "time": time}
            )
            self.write(
                {
                    'brauch_exported_file': base64.b64encode(
                        csv_data.encode()
                    ),
                    'brauch_exported_filename': csv_file_name,
                }
            )
            if self.carrier_id.prod_environment:
                self.carrier_id.with_delay()._brauch_push_to_ftp(
                    csv_data, csv_file_name
                )
        return {'exact_price': 0.0, 'tracking_number': False}

    def _brauch_write_csv_row(self, writer, package, pack_data):
        writer.writerow(pack_data)

    def _generate_brauch_csv(self):
        dialect = csv.excel
        dialect.delimiter = ";"
        columns = self.carrier_id._brauch_get_csv_columns()
        common_picking_data = self._brauch_get_common_picking_data()
        with StringIO() as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=columns, dialect=dialect
            )
            writer.writeheader()
            for pack in self.package_ids:
                pack_data = pack._brauch_get_pack_data(self)
                pack_data.update(common_picking_data.copy())
                self._brauch_write_csv_row(writer, pack, pack_data)
            csvfile.seek(0)
            csvdata = csvfile.read()
            return csvdata

    def _brauch_get_common_picking_data(self):
        auftrags_prio = (
            "Fixtermin" if self.sale_id.commitment_date else "Standard"
        )
        delivery_date = (
            self.sale_id.commitment_date
            or self.sale_id.expected_date
            or self.scheduled_date
        )
        date_done = self.date_done or self.scheduled_date
        return {
            "Verladedatum": date_done.strftime(
                self.carrier_id.brauch_datetime_format
            ),
            "Auftrags-Prio": auftrags_prio,
            "Lieferdatum": delivery_date.strftime(
                self.carrier_id.brauch_datetime_format
            ),
            "Lieferschein-Nr": self.name,
            "Tour": "",
            "Lieferant-Name": self.partner_id.display_name,
            "Lieferant-Strasse": self.partner_id.street or "",
            "Lieferant-Adres Zusatz": self.partner_id.street2 or "",
            "Lieferant-PLZ": self.partner_id.zip or "",
            "Lieferant-Ort": self.partner_id.city or "",
            "Auslieferhinweis (Info 2)": (
                self.partner_id.delivery_info_id.text or ""
            ).replace("\n", " "),
            "Lieferfenster": (
                self.partner_id.brauch_delivery_info or ""
            ).replace("\n", " "),
        }

    def _action_done(self):
        brauch_pickings = self.filtered(
            lambda p: p.carrier_id.delivery_type == "brauch"
        )
        if brauch_pickings:
            moves_lines_without_package = brauch_pickings.mapped(
                "move_line_ids_without_package"
            ).filtered(lambda ml: not ml.result_package_id)
            if moves_lines_without_package:
                raise UserError(
                    _(
                        "Following pickings are set to be delivered using 'Brauch'"
                        " carrier, but contain moves that are not in a package:"
                        "\n- %s" % "\n- ".join(brauch_pickings.mapped("name"))
                    )
                )
        return super()._action_done()