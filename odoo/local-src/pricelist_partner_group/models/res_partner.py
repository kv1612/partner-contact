# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, exceptions, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    factor_pricelist_item_id = fields.Many2one(
        string="Market Factor Applied",
        comodel_name="product.pricelist",
        compute="_compute_factor_pricelist_id",
    )
    partner_group_pricelist_id = fields.Many2one(
        string="Pricelist for partner group",
        comodel_name="product.pricelist",
        compute="_compute_partner_group_pricelist_id",
    )

    @api.depends("is_company", "company_group_id")
    def _compute_factor_pricelist_id(self):
        """Compute pricelist on partner.

        For a given partner, if part of a partner group,
        the applied pricelist is the group pricelist, otherwise,
        applied pricelist is it's own pricelist.
        """
        for record in self:
            record.factor_pricelist_item_id = False
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
            record.factor_pricelist_item_id = factor_item.base_pricelist_id.id

    @api.depends(
        "is_company",
        "company_group_id",
        "company_group_id.property_product_pricelist",
    )
    def _compute_partner_group_pricelist_id(self):
        for rec in self:
            rec.partner_group_pricelist_id = rec._get_partner_group_pricelist()

    def _get_partner_group_pricelist(self):
        """Retrieve pricelist by partner group if any.

        The rules for the pricelist are:

            * If the partner has a defined pricelist take it (meaning the
              pricelist if different from "Public Pricelist (CHF)")

            * Elif the partner has a company group,
              take the pricelist of it company group

            * Otherwise, take pricelist from partner
        """
        pricelist = None
        default_pricelist = self.env.ref(
            "product.list0", raise_if_not_found=False
        )
        if not default_pricelist:
            # For defensiveness... they shouldn't delete the Public Pricelist
            # but who knows. Without relying on the xmlid, it's hopefully a
            # good approximation to the "default" pricelist
            default_pricelist = self.env["product.pricelist"].search(
                [], limit=1
            )
        has_default_pricelist = (
            self.property_product_pricelist == default_pricelist
        )
        if has_default_pricelist and self.company_group_id:
            pricelist = self.company_group_id.property_product_pricelist
        return pricelist
