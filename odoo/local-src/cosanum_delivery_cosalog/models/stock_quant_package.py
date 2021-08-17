# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, models


class StockQuantPackage(models.Model):
    _inherit = "stock.quant.package"

    @api.depends(
        "packaging_id.packaging_type_id.code",
        "packaging_id.cosalog_number_of_parcels",
    )
    def _compute_display_name(self):
        # pylint: disable=missing-return
        # Override to display the list of CosaLog parcels if any
        for package in self:
            packaging = package.packaging_id
            if packaging.packaging_type_id.code == "CLOG":
                parcel_numbers = range(
                    1, packaging.cosalog_number_of_parcels + 1
                )
                names = [f"{package.name}-{i}" for i in parcel_numbers]
                package.display_name = ", ".join(names)
            else:
                super(StockQuantPackage, package)._compute_display_name()
