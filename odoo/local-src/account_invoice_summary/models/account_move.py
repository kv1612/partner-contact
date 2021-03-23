# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _report_has_ending_summaries(self):
        """Whether to display the section that contains the summaries"""
        self.ensure_one()
        return False
