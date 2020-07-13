# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, exceptions, models
from odoo.tools import float_compare

SINGLE_PRODUCT = "0_product_variant"
ALL_PRODUCTS = "3_global"


class ProductPricelist(models.Model):

    _inherit = "product.pricelist"

    def check_duplicate_item(self, vals):
        """Search existing product.pricelist.item records matching the vals."""
        domain = [
            (key, "=", val)
            for key, val in vals.items()
            if val and key not in ["price_discount", "fixed_price"]
        ]
        domain.append(("pricelist_id", "=", self.id))
        return self.env["product.pricelist.item"].search_count(domain)

    def filter_existing_items(self, item_vals):
        """Do not create a product.pricelist.item that already exists."""
        item_ids = []
        for item in item_vals:
            # (0, False, vals) tuples
            vals = item[2]
            existing_item = self.check_duplicate_item(vals)
            if existing_item:
                self.update_prices(existing_item, vals)
            else:
                item_ids.append(item)
        return item_ids

    def update_prices(self, item, vals):
        """Update pricelist item if prices was changed."""
        if vals.get("applied_on") == SINGLE_PRODUCT:
            new_price = vals.get("fixed_price")
            price_changed = new_price and float_compare(
                new_price, item.fixed_price, precision_digits=2
            )
            if price_changed:
                item.fixed_price = new_price
        else:
            new_discount = vals.get("price_discount")
            discount_changed = new_discount and float_compare(
                new_discount, item.price_discount, precision_digits=2
            )
            if discount_changed:
                item.price_discount = new_discount

    def write(self, vals):
        if self.env.context.get("load_csv"):
            item_vals = vals.get("item_ids")
            if item_vals:
                vals["item_ids"] = self.filter_existing_items(item_vals)
        return super().write(vals)

    @api.constrains("item_ids")
    def _check_qty_all_products_formulas(self):
        """Check there's at most one formula item applied to all products.
        """
        for record in self:
            formulas = record.item_ids.filtered(
                lambda i: i.compute_price == "formula"
                and i.applied_on == ALL_PRODUCTS
            )
            if len(formulas) > 1:
                raise exceptions.ValidationError(
                    _("There should be at most one factor price in pricelist")
                )

    @api.model
    def load(self, fields, data):
        return super(ProductPricelist, self.with_context(load_csv=True)).load(
            fields, data
        )
