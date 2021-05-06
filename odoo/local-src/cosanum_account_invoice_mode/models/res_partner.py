from odoo import api, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + [
            "invoicing_mode",
            "one_invoice_per_order",
        ]
