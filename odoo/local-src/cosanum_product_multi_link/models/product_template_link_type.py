# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, models
from odoo.exceptions import UserError


class ProductTemplateMultiLink(models.Model):
    _inherit = "product.template.link.type"

    @api.model
    def get_link_type(self, xmlid):
        link_type = self.env.ref(xmlid, raise_if_not_found=False)
        if not link_type:
            raise UserError(_("Product Link Type {} not found".format(xmlid)))
        return link_type
