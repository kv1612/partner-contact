# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    @api.model
    def _search(
        self,
        args,
        offset=0,
        limit=None,
        order=None,
        count=False,
        access_rights_uid=None,
    ):
        # Set an order to cancel the _search override in hr_holidays module
        # that order the records by remaining days instead of sequence
        if not order:
            order = self._order
        return super()._search(
            args, offset, limit, order, count, access_rights_uid
        )
