# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    report_cosalog_parcel_ids = fields.One2many(
        comodel_name="stock.quant.package",
        compute="_compute_report_cosalog_parcel_ids",
        string="CosaLog package parcels",
    )

    @api.depends("package_ids")
    def _compute_report_cosalog_parcel_ids(self):
        for picking in self:
            parcel_ids = []
            for package in picking.package_ids:
                # The number of package reports to print is defined by the
                # number of CosaLog parcels configured in its packaging.
                # This means that we will have duplicated package records in
                # the parcels recordsets: it's on purpose!
                packaging = package.packaging_id
                if packaging.packaging_type_id.code == "CLOG":
                    # NOTE: even for CosaLog packages configured with a number
                    # of parcels of 0 we consider it is 1 to also print them.
                    # Such parcels will be printed differently than others to
                    # identify them easily.
                    nb_of_parcels = packaging.cosalog_number_of_parcels or 1
                    parcel_ids.extend(package.ids * nb_of_parcels)
            parcels = self.env["stock.quant.package"].browse(parcel_ids)
            picking.report_cosalog_parcel_ids = parcels
