# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.tests.common import Form, SavepointCase


class TestSaleOnchangePartnerSetPricelist(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        field = cls.env['ir.model.fields'].search(
            [
                ('model', '=', 'res.partner'),
                ('name', '=', 'property_product_pricelist'),
            ]
        )
        cls.env['ir.property'].search(
            [('fields_id', '=', field.id), ('res_id', '=', False)]
        ).unlink()
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.partner_group = cls.env["res.partner"].create(
            {"name": "Test Group"}
        )
        cls.custom_pricelist = cls.env["product.pricelist"].create(
            {"name": "Test Pricelist"}
        )

    def test_default_pricelist(self):
        """No group and use default partner pricelist"""
        pricelist = self.partner.property_product_pricelist
        sale_form = Form(self.env["sale.order"])
        sale_form.partner_id = self.partner
        self.assertEqual(sale_form.pricelist_id, pricelist)

    def test_partner_pricelist(self):
        """No group and pricelist set on partner: use it"""
        self.partner.property_product_pricelist = self.custom_pricelist
        sale_form = Form(self.env["sale.order"])
        sale_form.partner_id = self.partner
        self.assertEqual(sale_form.pricelist_id, self.custom_pricelist)

    def test_partner_group_pricelist_partner_first(self):
        """Group and pricelist set on partner: use it"""
        self.partner.company_group_id = self.partner_group
        self.partner.property_product_pricelist = self.custom_pricelist
        sale_form = Form(self.env["sale.order"])
        sale_form.partner_id = self.partner
        self.assertEqual(sale_form.pricelist_id, self.custom_pricelist)

    def test_partner_group_pricelist(self):
        """Group and no pricelist set on partner: use the group's one"""
        self.partner.company_group_id = self.partner_group
        self.partner_group.property_product_pricelist = self.custom_pricelist
        sale_form = Form(self.env["sale.order"])
        sale_form.partner_id = self.partner
        self.assertEqual(sale_form.pricelist_id, self.custom_pricelist)
