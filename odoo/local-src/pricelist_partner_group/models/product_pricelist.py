# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, models


class ProductPricelist(models.Model):

    _inherit = "product.pricelist"

    def check_duplicate_item(self, vals):
        """
        Search and returns existing product.pricelist.item
        matching the vals passed as argument.
        """
        domain = [(key, "=", val) for key, val in vals.items() if val]
        return self.env["product.pricelist.item"].search(domain)

    def filter_existing_items(self, item_vals):
        """
        Do not create a product.pricelist.item that already exists.
        """
        item_ids = []
        for item in item_vals:
            if self.check_duplicate_item(item[2]):
                continue
            item_ids.append(item)
        return item_ids

    def write(self, vals):
        if self.env.context.get("load_csv"):
            item_vals = vals.get("item_ids")
            if item_vals:
                vals["item_ids"] = self.filter_existing_items(item_vals)
        return super().write(vals)

    @api.model
    def load(self, fields, data):
        return super(ProductPricelist, self.with_context(load_csv=True)).load(
            fields, data
        )
