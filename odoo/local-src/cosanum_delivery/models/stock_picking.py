# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
import os

from odoo import fields, models, tools

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    carrier_id = fields.Many2one(tracking=True)

    def send_to_shipper(self):
        # Overridden to prevent sending data to the shipper (to print labels
        # for instance) in a dev environment.
        # It is actually blocking the validation of DHL transfers but it could
        # block others carrier integrations because they are all built the same
        # way in odoo/enterprise (delivery_dhl, delivery_ups...).
        if (
            os.getenv("RUNNING_ENV") == "dev"
            and not tools.config['test_enable']
            # Exception for Brauch and Cosanum as we generate a CSV file which can not
            # be sent on the SFTP (disabled on dev by server_env)
            and self.carrier_id.delivery_type not in ["brauch", "cosanum"]
        ):
            _logger.info("DEV MODE detected: skip send shipping")
            return
        return super().send_to_shipper()
