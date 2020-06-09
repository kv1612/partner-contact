# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, exceptions, models


class ProductPricelistItem(models.Model):

    _inherit = "product.pricelist.item"

    @api.constrains("base_pricelist_id", "pricelist_id")
    def _check_base_pricelist_id(self):
        """
        A pricelist item can refer to another pricelist through `base_pricelist_id`.
        When computing the price of a product, an infinite recursion can appears.
        That rule is here to avoid recursions in such a case.
        => The base pricelist cannot be based on another pricelist.
        """
        default_pricelist = self.env.ref("product.list0")
        for record in self:
            if (
                record.base_pricelist_id
                and record.pricelist_id == default_pricelist
            ):
                raise exceptions.ValidationError(
                    _(
                        "{} items shouldn't be based on any other pricelist"
                    ).format(default_pricelist.name)
                )
