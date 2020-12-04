# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplateMultiLink(models.Model):

    _inherit = "product.template.link"

    mandatory_start_date = fields.Boolean(
        compute="_compute_mandatory_start_date"
    )

    @api.depends("type_id")
    def _compute_mandatory_start_date(self):
        alternative_type = self.env[
            'product.template.link.type'
        ].get_type_alternative()
        for rec in self:
            rec.mandatory_start_date = rec.type_id == alternative_type
