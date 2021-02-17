# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ProductPackaging(models.Model):
    _inherit = "product.packaging"

    packaging_type_code = fields.Char(related="packaging_type_id.code")
    cosalog_number_of_parcels = fields.Integer(
        string="CosaLog: Number of Parcels", default=1
    )
