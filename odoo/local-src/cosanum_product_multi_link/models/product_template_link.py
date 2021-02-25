# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import _, api, exceptions, fields, models


class ProductTemplateLink(models.Model):

    _inherit = "product.template.link"

    pricelist_replaced = fields.Boolean(
        "Pricelists items replaced", copy=False
    )

    def check_link_type(self, link_type):
        self.ensure_one()
        if self.type_id != link_type:
            raise exceptions.UserError(
                _(
                    "You can only duplicate automatically the "
                    "pricelist items for replacement link types"
                )
            )

    def check_already_replaced(self):
        self.ensure_one()
        if self.pricelist_replaced:
            raise exceptions.UserError(
                _(
                    "The pricelist lines for this link has already "
                    "been duplicated. If you made an error on the product, "
                    "you have to manually fix the pricelists items."
                )
            )

    def check_linked_product_and_template_set(self):
        self.ensure_one()
        right_product_and_variant_set = (
            self.right_product_tmpl_id and self.right_product_id
        )
        if not right_product_and_variant_set:
            raise exceptions.UserError(
                _(
                    "You need to set the linked product and/or variant "
                    "before using the pricelists items duplication"
                )
            )

    def check_source_product_and_template_set(self):
        self.ensure_one()
        left_product_and_variant_set = (
            self.left_product_tmpl_id and self.left_product_id
        )
        if not left_product_and_variant_set:
            raise exceptions.UserError(
                _(
                    "You need to set the source product and/or variant "
                    "before using the pricelists items duplication"
                )
            )

    def check_pricelist_duplication_conditions(self):
        """
        - link type should be replacement
        - pricelist should not have already been replaced
        - at least source template or product should be set
        - at least linked template or product should be set
        """
        replacement_type = self.env["product.template.link.type"].get_by_code(
            "replacement"
        )
        for record in self:
            record.check_link_type(replacement_type)
            record.check_already_replaced()
            record.check_linked_product_and_template_set()
            record.check_source_product_and_template_set()

    @api.model
    def make_duplication(self, items, values):
        for item in items:
            item.copy(values)

    def duplicate_pricelist_items(self):
        self.ensure_one()
        pricelist_item_model = self.env["product.pricelist.item"]
        for record in self:
            # First, duplicate variant pricelist items
            variant_vals = {
                "product_tmpl_id": record.right_product_tmpl_id.id,
                "product_id": record.right_product_id.id,
            }
            variant_items = pricelist_item_model.search(
                [
                    ("product_id", "=", record.left_product_id.id),
                    ("applied_on", "=", "0_product_variant"),
                ]
            )
            record.make_duplication(variant_items, variant_vals)
            # Then, duplicate template pricelist items
            tmpl_vals = {"product_tmpl_id": record.right_product_tmpl_id.id}
            tmpl_items = pricelist_item_model.search(
                [
                    ("product_tmpl_id", "=", record.left_product_tmpl_id.id),
                    ("applied_on", "=", "1_product"),
                    # We do not want to pick a wrong variant by error
                    ("product_id", "=", False),
                ]
            )
            record.make_duplication(tmpl_items, tmpl_vals)
            # If everything's right, set link as already processed
            record.pricelist_replaced = True

    def action_duplicate_pricelist_items(self):
        self.check_pricelist_duplication_conditions()
        self.duplicate_pricelist_items()
