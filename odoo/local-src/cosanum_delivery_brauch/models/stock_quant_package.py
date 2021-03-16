# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import models


class StockQuantPackage(models.Model):

    _inherit = "stock.quant.package"

    def _brauch_get_pack_data(self):
        res = super()._brauch_get_pack_data()
        res["Package Code"] = self.packaging_id.shipper_package_code or ""
        return res
