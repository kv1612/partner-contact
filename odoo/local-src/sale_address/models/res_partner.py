# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Contact(models.Model):
    _inherit = 'res.partner'

    partner_shipping_id = fields.Many2one(
        'res.partner', 'Shipping Partner', ondelete='set null'
    )
    partner_invoicing_id = fields.Many2one(
        'res.partner', 'Invoicing Partner', ondelete='set null'
    )
