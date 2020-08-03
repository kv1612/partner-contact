# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tests.common import Form, SavepointCase
from odoo.tools import convert_file

DATA_FILES = [
    "tests/data/res.partner.industry.csv",
    "tests/data/product.pricelist.csv",
    "tests/data/product.product.csv",
    "tests/data/res.partner.csv",
    "tests/data/product.pricelist.item.csv",
]


class TestPricelist(SavepointCase):
    at_install = False
    post_install = True

    def _create_order(self, partner, products):
        """
        Creates a sale order given a customer and a list of products.
        """
        sale_form = Form(self.env["sale.order"])
        sale_form.partner_id = partner
        for product in products:
            with sale_form.order_line.new() as line:
                line.product_id = product
        return sale_form.save()

    def _check_order_prices(self, order, prices_mapping):
        """
        Given a list of (product, price) mapping, check that orer lines price units
        are valid.
        """
        for product, price in prices_mapping:
            line = order.order_line.filtered(lambda l: l.product_id == product)
            self.assertEqual(line.price_unit, price)

    def check_pricelist_items(self, pricelist, items_mapping):
        """
        Given a list of (product, nb_lines, price), check that pricelist items
        are created or not when needed.
        """
        for product, nb_lines, price in items_mapping:
            item = pricelist.item_ids.filtered(
                lambda i: i.product_id == product
            )
            self.assertEqual(len(item), nb_lines)
            if price is not None:
                self.assertEqual(item.fixed_price, price)

    @classmethod
    def set_currency(cls):
        """
        Sets the same currency for user than the one set on records created from csv.
        """
        cls.env.user.company_id.currency_id = cls.env.ref("base.USD")

    @classmethod
    def load_data(cls):
        cr = cls.env.cr
        for filename in DATA_FILES:
            convert_file(cr, "pricelist_partner_group", filename, None)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.set_currency()
        # Load data
        cls.load_data()
        # Get products
        cls.product_00 = cls.env.ref("pricelist_partner_group.product_00")
        cls.product_01 = cls.env.ref("pricelist_partner_group.product_01")
        cls.product_02 = cls.env.ref("pricelist_partner_group.product_02")
        cls.product_03 = cls.env.ref("pricelist_partner_group.product_03")
        cls.product_04 = cls.env.ref("pricelist_partner_group.product_04")
        cls.product_05 = cls.env.ref("pricelist_partner_group.product_05")
        cls.product_06 = cls.env.ref("pricelist_partner_group.product_06")
        cls.product_07 = cls.env.ref("pricelist_partner_group.product_07")
        cls.product_08 = cls.env.ref("pricelist_partner_group.product_08")
        cls.product_09 = cls.env.ref("pricelist_partner_group.product_09")
        cls.product_10 = cls.env.ref("pricelist_partner_group.product_10")
        cls.product_11 = cls.env.ref("pricelist_partner_group.product_11")
        cls.product_12 = cls.env.ref("pricelist_partner_group.product_12")
        # Pricelists industries configuration
        industries = cls.env["res.partner.industry"]
        industries |= cls.env.ref("pricelist_partner_group.industry_hospital")
        industries |= cls.env.ref("pricelist_partner_group.industry_ems")
        company = cls.env["res.company"].search([])
        company.write({"pricelist_industry_ids": [(6, 0, industries.ids)]})

    def test_pricelist_partner_group(self):
        self.case_01()
        self.case_02()
        self.case_03()
        self.case_04()
        self.case_05()
        self.case_06()
        self.case_07()
        self.case_08()
        self.case_09()
        self.case_10()
        self.case_11()

    def case_01(self):
        customer = self.env.ref("pricelist_partner_group.customer_00")
        pricelist = customer.property_product_pricelist
        products = [self.product_00, self.product_02]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_00, 110), (self.product_02, 128)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [(self.product_00, 1, 110)]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_02(self):
        customer = self.env.ref("pricelist_partner_group.customer_01")
        products = [self.product_00, self.product_03]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_00, 90), (self.product_03, 12.6)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()

    def case_03(self):
        customer = self.env.ref("pricelist_partner_group.customer_02")
        pricelist = customer.property_product_pricelist
        products = [self.product_00]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_00, 120)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [(self.product_00, 1, 120)]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_04(self):
        customer = self.env.ref("pricelist_partner_group.customer_03")
        products = [self.product_00]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_00, 100)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()

    def case_05(self):
        customer = self.env.ref("pricelist_partner_group.customer_05")
        pricelist = customer.company_group_id.property_product_pricelist
        products = [
            self.product_05,
            self.product_02,
            self.product_00,
            self.product_12,
        ]
        order = self._create_order(customer, products)
        prices_mapping = [
            (self.product_05, 85.12),
            (self.product_02, 118.96),
            (self.product_00, 90),
            (self.product_12, 70.35),
        ]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [(self.product_00, 1, 90)]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_06(self):
        customer = self.env.ref("pricelist_partner_group.customer_06")
        pricelist = customer.company_group_id.property_product_pricelist
        products = [
            self.product_05,
            self.product_12,
            self.product_02,
            self.product_00,
        ]
        order = self._create_order(customer, products)
        prices_mapping = [
            (self.product_05, 90.72),
            (self.product_12, 59.12),
            (self.product_02, 118.96),
            (self.product_00, 90),
        ]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [(self.product_05, 1, 90.72)]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_07(self):
        customer = self.env.ref("pricelist_partner_group.customer_07")
        products = [
            self.product_10,
            self.product_12,
            self.product_00,
            self.product_05,
        ]
        order = self._create_order(customer, products)
        prices_mapping = [
            (self.product_10, 2.38),
            (self.product_12, 70.35),
            (self.product_00, 90),
            (self.product_05, 90.72),
        ]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()

    def case_08(self):
        customer = self.env.ref("pricelist_partner_group.customer_09")
        pricelist = customer.company_group_id.property_product_pricelist
        products = [self.product_01, self.product_00]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_01, 2.93), (self.product_00, 100)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [
            (self.product_01, 0, None),
            (self.product_00, 0, None),
        ]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_09(self):
        customer = self.env.ref("pricelist_partner_group.customer_10")
        pricelist = customer.company_group_id.property_product_pricelist
        products = [self.product_01, self.product_00]
        order = self._create_order(customer, products)
        prices_mapping = [(self.product_01, 7.17), (self.product_00, 100)]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [
            (self.product_01, 0, None),
            (self.product_00, 0, None),
        ]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_10(self):
        customer = self.env.ref("pricelist_partner_group.customer_12")
        pricelist = customer.company_group_id.property_product_pricelist
        products = [self.product_12, self.product_00, self.product_06]
        order = self._create_order(customer, products)
        prices_mapping = [
            (self.product_12, 46),
            (self.product_00, 90),
            (self.product_06, 14),
        ]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
        items_mapping = [(self.product_00, 1, 90)]
        self.check_pricelist_items(pricelist, items_mapping)

    def case_11(self):
        customer = self.env.ref("pricelist_partner_group.customer_13")
        products = [self.product_12, self.product_11, self.product_06]
        order = self._create_order(customer, products)
        prices_mapping = [
            (self.product_12, 46),
            (self.product_11, 5.13),
            (self.product_06, 16.96),
        ]
        self._check_order_prices(order, prices_mapping)
        order.action_confirm()
