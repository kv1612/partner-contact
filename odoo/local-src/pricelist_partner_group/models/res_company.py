# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    pricelist_industry_ids = fields.Many2many(
        "res.partner.industry",
        help="Industries for which fixed prices are automatically set",
    )
