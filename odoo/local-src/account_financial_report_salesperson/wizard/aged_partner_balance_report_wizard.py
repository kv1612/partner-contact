# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AgedPartnerBalanceReportWizard(models.TransientModel):
    """Aged partner balance report wizard."""

    _description = 'Aged Partner Balance Report Wizard'
    _inherit = 'aged.partner.balance.report.wizard'

    # OCA change the name of the model to add "report" but nothing in xml

    user_id = fields.Many2one(comodel_name='res.users', string='Salesman')

    @api.onchange('user_id')
    def onchange_user_id(self):
        """ Set partner_ids where the user_is is the Salesman """
        if self.user_id:
            # cosanum work on b2b and b2c so we want :
            # all companies or individuals without parent_id
            domain = [
                '&',
                ('user_id', '=', self.user_id.id),
                '|',
                ('is_company', '=', True),
                ('parent_id', '=', False),
            ]
            self.partner_ids = self.env['res.partner'].search(domain)
        else:
            self.partner_ids = False

    @api.onchange("receivable_accounts_only", "payable_accounts_only")
    def onchange_type_accounts_only(self):

        domain = [("company_id", "=", self.company_id.id)]
        if (
            not self.receivable_accounts_only
            and not self.payable_accounts_only
        ):
            domain += [("reconcile", "=", True)]
            self.account_ids = self.env["account.account"].search(domain)
            return
        return super().onchange_type_accounts_only()
