# Copyright 2021 Camptocamp SA (http2://www.camptocamp.com)
# License AGPL-3.0 or later (http2://www.gnu.org/licenses/agpl.html)
from psycopg2 import IntegrityError

from odoo.tests.common import SavepointCase
from odoo.tools import mute_logger


class TestResPartnerDeliveryInfo(SavepointCase):
    def test_unlink(self):
        delivery_info = self.env["res.partner.delivery.info"].create(
            {"name": "Test Name", "text": "Test Text"}
        )
        partner = self.env.ref("base.res_partner_3")
        partner.delivery_info_id = delivery_info
        self.assertTrue(delivery_info.active)
        self.assertEqual(partner.delivery_info_id, delivery_info)
        with mute_logger("odoo.sql_db"):
            with self.assertRaises(IntegrityError):
                delivery_info.unlink()
