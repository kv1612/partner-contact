# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class StockPicking(models.Model):

    _inherit = "stock.picking"

    def _brauch_get_common_picking_data(self):
        res = super()._brauch_get_common_picking_data()
        schlieren_wh = self.env.ref(
            "stock.warehouse0", raise_if_not_found=False
        )
        werrikon_wh = self.env.ref(
            "cosanum_base.warehouse_wer", raise_if_not_found=False
        )
        wh = self.picking_type_id.warehouse_id
        res["Schlieren"] = "10" if wh == schlieren_wh else ""
        res["Werrikon"] = "20" if wh == werrikon_wh else ""
        return res
