# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, _


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    @api.multi
    def _prepare_holidays_meeting_values(self):
        values = super()._prepare_holidays_meeting_values()
        values.update(
            {'name': _('On leave'),
             'description': '',
             }
        )
        return values
