# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.exceptions import UserError

from .common import CommonTestLinkPricelist


class TestLinkPricelistDuplicate(CommonTestLinkPricelist):
    def test_link_pricelist_duplicate_no_tmpl_on_pricelist_item(self):
        """
        If only variant is set on item, copy linked template and variant
        """
        self.replacement_link_1.action_duplicate_pricelist_items()
        new_items = self.env["product.pricelist.item"].search(
            [
                (
                    "product_id",
                    "=",
                    self.replacement_link_1.right_product_id.id,
                ),
                (
                    "product_tmpl_id",
                    "=",
                    self.replacement_link_1.right_product_tmpl_id.id,
                ),
            ]
        )
        self.assertEqual(len(new_items), 1)

    def test_link_pricelist_duplicate_pricelist_item(self):
        """
        If both variant and template are set on item, copy linked variant and template
        """
        self.replacement_link_2.action_duplicate_pricelist_items()
        new_items = self.env["product.pricelist.item"].search(
            [
                (
                    "product_id",
                    "=",
                    self.replacement_link_2.right_product_id.id,
                ),
                (
                    "product_tmpl_id",
                    "=",
                    self.replacement_link_2.right_product_tmpl_id.id,
                ),
            ]
        )
        self.assertEqual(len(new_items), 1)

    def test_link_pricelist_duplicate_only_tmpl_on_pricelist_item(self):
        """
        If only tmpl set on item, only linked tmpl is copied, variant is False
        """
        self.replacement_link_3.action_duplicate_pricelist_items()
        new_items = self.env["product.pricelist.item"].search(
            [
                ("product_id", "=", False),
                (
                    "product_tmpl_id",
                    "=",
                    self.replacement_link_3.right_product_tmpl_id.id,
                ),
            ]
        )
        self.assertEqual(len(new_items), 1)

    def test_exceptions(self):
        """
        - if link type is not replacement, should raise an exception
        - if pricelist already copied, should raise an exception
        """
        with self.assertRaises(UserError):
            # wrong link type
            self.replacement_link_4.action_duplicate_pricelist_items()
        self.replacement_link_4.type_id = self.link_type_replacement
        self.replacement_link_4.action_duplicate_pricelist_items()
        with self.assertRaises(UserError):
            # link already processed
            self.replacement_link_4.action_duplicate_pricelist_items()
