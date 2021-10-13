# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id() or {}
        values = {}
        partner = self.partner_id.commercial_partner_id
        if partner:
            if partner.partner_invoicing_id:
                values['partner_invoice_id'] = partner.partner_invoicing_id.id
            if partner.partner_shipping_id:
                values['partner_shipping_id'] = partner.partner_shipping_id.id
        if values:
            self.update(values)
            res["value"] = dict(res.get("value", {}), **values)
        return res