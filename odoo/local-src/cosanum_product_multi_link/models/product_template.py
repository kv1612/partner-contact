# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def get_product_replacement(self):
        """Get all active replacement for the product."""
        self.ensure_one()
        replacement_type = self.env[
            'product.template.link.type'
        ].get_type_replacement()
        replacement = self.product_template_link_ids.filtered(
            lambda r: r.type_id == replacement_type and r.is_link_active
        )
        return replacement
