# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    vendor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor',
        domain=[('supplier_rank', '>', 0)],
    )

    # field overloading from text to html
    description = fields.Html()
