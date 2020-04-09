# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class OpenItemsReportWizard(models.TransientModel):
    """Open items report wizard."""

    _description = "Open Items Report Wizard"
    _inherit = 'open.items.report.wizard'

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
