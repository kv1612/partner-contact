# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_fee_line_qty_from_out_package(
        self, package_fee, picking, package
    ):
        # Override to compute the fee qty based on the number of
        # CosaLog parcels of the package
        packaging = package.packaging_id
        if packaging.packaging_type_id.code == "CLOG":
            return packaging.cosalog_number_of_parcels
        return super()._get_fee_line_qty_from_out_package(
            package_fee, picking, package
        )
