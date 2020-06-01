# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    pricelist_industry_ids = fields.Many2many(
        "res.partner.industry",
        related="company_id.pricelist_industry_ids",
        readonly=False,
    )
