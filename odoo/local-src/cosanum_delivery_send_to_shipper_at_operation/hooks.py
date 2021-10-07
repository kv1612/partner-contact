# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import tools


def update_data(cr, registry):
    """Force the update of XML records as they are flagged as 'noupdate'."""
    tools.convert.convert_file(
        cr,
        "cosanum_delivery_send_to_shipper_at_operation",
        "data/delivery_carrier.xml",
        None,
        mode="init",
        kind="data",
    )
