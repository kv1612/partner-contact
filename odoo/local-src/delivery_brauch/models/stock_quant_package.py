# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class StockQuantPackage(models.Model):

    _inherit = "stock.quant.package"

    def _brauch_get_pack_data(self):
        return {
            "Ist-Anz. Pal.": 1,
            "K-PID": self.name,
            "Gewicht (kg)": self.shipping_weight,
        }
