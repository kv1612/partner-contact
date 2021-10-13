# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)
from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _validate_invoice(self):
        # Invoices have to be generated even if the job has been spawn
        # by a non-account user.
        # FIXME: to include upstream?
        self = self.sudo()
        return super()._validate_invoice()
