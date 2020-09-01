# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models
from odoo.addons.queue_job.job import job, related_action


class AccountMove(models.Model):
    _inherit = "account.move"

    @job(default_channel="root.invoice_validation")
    @related_action(action="related_action_open_invoice")
    def _validate_invoice(self):
        # Invoices have to be generated even if the job has been spawn
        # by a non-account user.
        # FIXME: to include upstream?
        self = self.sudo()
        return super()._validate_invoice()
