# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def _get_sales_order_to_invoice(self):
        """Get all sale order grouped in the picking."""
        return self.sale_ids
