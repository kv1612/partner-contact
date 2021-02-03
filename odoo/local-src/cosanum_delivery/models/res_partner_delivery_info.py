# Copyright 2021 Camptocamp SA (https://www.camptocamp.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResPartnerDeliveryInfo(models.Model):
    _name = "res.partner.delivery.info"
    _description = "Delivery Indications by Customer to Carrier"

    name = fields.Char("Name", required=True)
    text = fields.Text("Text", required=True)
    active = fields.Boolean("Active", default=True)

    def unlink(self):  # pylint: disable=W8106
        """Archive, not unlink"""
        self.write({"active": False})

    def toggle_active(self):
        for record in self:
            record.active = not record.active
