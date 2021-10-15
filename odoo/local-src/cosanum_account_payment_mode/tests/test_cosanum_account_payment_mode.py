# Copyright 2020 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl)
from odoo.tests.common import Form, SavepointCase


class TestCosanumPaymentMode(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.partner_1 = cls.env.ref("base.res_partner_1")
        cls.partner_2 = cls.env.ref("base.res_partner_2")
        cls.bank_account_1 = cls.env["res.partner.bank"].create(
            {
                "acc_number": "CH1234567890",
                "partner_id": cls.env.user.company_id.id,
            }
        )
        cls.bank_account_2 = cls.env["res.partner.bank"].create(
            {
                "acc_number": "CH0987654321",
                "partner_id": cls.env.user.company_id.id,
            }
        )
        cls.account_journal_1 = cls.env["account.journal"].create(
            {
                "name": "Journal 1",
                "code": "J1",
                "type": "sale",
                "bank_account_id": cls.bank_account_1.id,
            }
        )
        cls.account_journal_2 = cls.env["account.journal"].create(
            {
                "name": "Journal 2",
                "code": "J2",
                "type": "sale",
                "bank_account_id": cls.bank_account_2.id,
            }
        )
        cls.payment_mode_1 = cls.env.ref(
            "account_payment_mode.payment_mode_outbound_dd1"
        )
        cls.payment_mode_1.fixed_journal_id = cls.account_journal_1
        cls.payment_mode_1.bank_account_link = "fixed"
        cls.payment_mode_1.payment_type = "inbound"
        cls.payment_mode_2 = cls.env.ref(
            "account_payment_mode.payment_mode_outbound_dd2"
        )
        cls.payment_mode_2.fixed_journal_id = cls.account_journal_2
        cls.payment_mode_1.bank_account_link = "fixed"
        cls.payment_mode_2.payment_type = "inbound"
        cls.partner_1.customer_payment_mode_id = cls.payment_mode_1
        cls.partner_2.customer_payment_mode_id = cls.payment_mode_2
        cls.invoice = cls.env["account.move"].create(
            {"partner_id": cls.partner_1.id, "move_type": "out_invoice"}
        )

    def test_invoice_partner_bank_set_on_payment_mode_change(self):
        """Check bank account is selected on payment mode change."""
        self.assertEqual(self.invoice.payment_mode_id, self.payment_mode_1)
        self.assertEqual(self.invoice.partner_bank_id, self.bank_account_1)
        self.invoice.payment_mode_id = self.payment_mode_2
        self.assertEqual(self.invoice.partner_bank_id, self.bank_account_2)

    def test_invoice_partner_bank_set_on_partner_change(self):
        """Check payment mode and bank account are selected on customer change."""
        self.invoice.partner_id = self.partner_2
        self.assertEqual(self.invoice.payment_mode_id, self.payment_mode_2)
        self.assertEqual(self.invoice.partner_bank_id, self.bank_account_2)

    def test_invoice_partner_bank_in_form(self):
        """Check bank account is set correctely in the view."""
        form = Form(self.invoice)
        self.assertEqual(form.payment_mode_id, self.payment_mode_1)
        self.assertEqual(self.invoice.partner_bank_id, self.bank_account_1)
        # Test changing the payment_mode
        form.payment_mode_id = self.payment_mode_2
        self.assertEqual(form.partner_bank_id, self.bank_account_2)
        form.payment_mode_id = self.payment_mode_1
        self.assertEqual(form.partner_bank_id, self.bank_account_1)
        # Test changing the partner
        form.partner_id = self.partner_2
        self.assertEqual(form.payment_mode_id, self.payment_mode_2)
        self.assertEqual(form.partner_bank_id, self.bank_account_2)
