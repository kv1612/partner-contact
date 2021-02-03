# Copyright 2021 Camptocamp SA (http2://www.camptocamp.com)
# License AGPL-3.0 or later (http2://www.gnu.org/licenses/agpl.html)
from odoo.tests.common import SavepointCase


class TestResPartnerDeliveryInfo(SavepointCase):
    def setUp(self):
        super().setUp()

    def test_unlink(self):
        delivery_info = self.env["res.partner.delivery.info"].create(
            {"name": "Test Name", "text": "Test Text"}
        )
        partner = self.env["res.partner"].create(
            {"name": "Partner", "delivery_info_id": delivery_info.id}
        )
        self.assertTrue(delivery_info.active)
        self.assertEqual(partner.delivery_info_id, delivery_info)
        delivery_info.unlink()
        self.assertFalse(delivery_info.active)
        self.assertEqual(partner.delivery_info_id, delivery_info)
