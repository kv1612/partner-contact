# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, exceptions, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    factor_pricelist_item = fields.Many2one(
        string="Market Factor Applied",
        comodel_name="product.pricelist",
        compute="_compute_factor_pricelist",
    )

    @api.depends("is_company", "company_group_id")
    def _compute_factor_pricelist(self):
        """Compute pricelist on partner.

        For a given partner, if part of a partner group,
        the applied pricelist is the group pricelist, otherwise,
        applied pricelist is it's own pricelist.
        """
        for record in self:
            record.factor_pricelist_item = False
            if not record.is_company:
                continue
            if record.company_group_id:
                pricelist = record.company_group_id.property_product_pricelist
            else:
                pricelist = record.property_product_pricelist
            factor_item = pricelist.item_ids.filtered(
                lambda i: i.compute_price == "formula"
                # pricelist items applied on all products
                and i.applied_on == "3_global"
            )
            if len(factor_item) > 1:
                raise exceptions.UserError(
                    _(
                        "There is more than one factor price in pricelist {}"
                    ).format(pricelist.name)
                )
            record.factor_pricelist_item = factor_item.base_pricelist_id.id
