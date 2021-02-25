# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tests.common import SavepointCase


class CommonTestLinkPricelist(SavepointCase):
    at_install = False
    post_install = True

    @classmethod
    def setUpProducts(cls):
        cls.product_replaced_1 = cls.env["product.product"].create(
            {"name": "Replaced Product 1"}
        )
        cls.product_replaced_2 = cls.env["product.product"].create(
            {"name": "Replaced Product 2"}
        )
        cls.product_replaced_3 = cls.env["product.product"].create(
            {"name": "Replaced Product 3"}
        )
        cls.product_replaced_4 = cls.env["product.product"].create(
            {"name": "Replaced Product 4"}
        )
        cls.product_replacement_1 = cls.env["product.product"].create(
            {"name": "replacement Product 1"}
        )
        cls.product_replacement_2 = cls.env["product.product"].create(
            {"name": "replacement Product 2"}
        )
        cls.product_replacement_3 = cls.env["product.product"].create(
            {"name": "replacement Product 3"}
        )
        cls.product_replacement_4 = cls.env["product.product"].create(
            {"name": "replacement Product 4"}
        )
        cls.template_replaced_1 = cls.product_replaced_1.product_tmpl_id
        cls.template_replaced_2 = cls.product_replaced_2.product_tmpl_id
        cls.template_replaced_3 = cls.product_replaced_3.product_tmpl_id
        cls.template_replaced_4 = cls.product_replaced_4.product_tmpl_id
        cls.template_replacement_1 = cls.product_replacement_1.product_tmpl_id
        cls.template_replacement_2 = cls.product_replacement_2.product_tmpl_id
        cls.template_replacement_3 = cls.product_replacement_3.product_tmpl_id
        cls.template_replacement_4 = cls.product_replacement_4.product_tmpl_id

    @classmethod
    def setUpPricelists(cls):
        cls.pricelist = cls.env.ref("product.list0")
        pricelist_item_vals = [
            (
                0,
                0,
                {
                    "applied_on": "0_product_variant",
                    "product_id": cls.product_replaced_1.id,
                    "compute_price": "fixed",
                    "fixed_price": 99,
                },
            ),
            (
                0,
                0,
                {
                    "applied_on": "0_product_variant",
                    "product_id": cls.product_replaced_2.id,
                    "product_tmpl_id": cls.template_replaced_2.id,
                    "compute_price": "fixed",
                    "fixed_price": 99,
                },
            ),
            (
                0,
                0,
                {
                    "applied_on": "1_product",
                    "product_tmpl_id": cls.template_replaced_1.id,
                    "compute_price": "fixed",
                    "fixed_price": 99,
                },
            ),
            (
                0,
                0,
                {
                    "applied_on": "1_product",
                    "product_tmpl_id": cls.template_replaced_3.id,
                    "product_id": cls.product_replaced_3.id,
                    "compute_price": "fixed",
                    "fixed_price": 99,
                },
            ),
        ]
        cls.pricelist.write({"item_ids": pricelist_item_vals})

    @classmethod
    def setUpLinks(cls):
        link_type_model = cls.env["product.template.link.type"]
        cls.link_type_xsell = link_type_model.get_by_code("cross-selling")
        cls.link_type_replacement = link_type_model.get_by_code("replacement")
        cls.replacement_link_1 = cls.env["product.template.link"].create(
            {
                "left_product_id": cls.product_replaced_1.id,
                "right_product_id": cls.product_replacement_1.id,
                "left_product_tmpl_id": cls.template_replaced_1.id,
                "right_product_tmpl_id": cls.template_replacement_1.id,
                "type_id": cls.link_type_replacement.id,
            }
        )
        cls.replacement_link_2 = cls.env["product.template.link"].create(
            {
                "left_product_id": cls.product_replaced_2.id,
                "right_product_id": cls.product_replacement_2.id,
                "left_product_tmpl_id": cls.template_replaced_2.id,
                "right_product_tmpl_id": cls.template_replacement_2.id,
                "type_id": cls.link_type_replacement.id,
            }
        )
        cls.replacement_link_3 = cls.env["product.template.link"].create(
            {
                "left_product_id": cls.product_replaced_3.id,
                "right_product_id": cls.product_replacement_3.id,
                "left_product_tmpl_id": cls.template_replaced_3.id,
                "right_product_tmpl_id": cls.template_replacement_3.id,
                "type_id": cls.link_type_replacement.id,
            }
        )
        cls.replacement_link_4 = cls.env["product.template.link"].create(
            {
                "left_product_id": cls.product_replaced_4.id,
                "right_product_id": cls.product_replacement_4.id,
                "left_product_tmpl_id": cls.template_replaced_4.id,
                "right_product_tmpl_id": cls.template_replacement_4.id,
                "type_id": cls.link_type_xsell.id,
            }
        )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.setUpProducts()
        cls.setUpPricelists()
        cls.setUpLinks()
