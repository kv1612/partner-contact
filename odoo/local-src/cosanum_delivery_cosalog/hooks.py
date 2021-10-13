# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import tools


def update_data(cr, registry):
    """Force the update of XML records as they are flagged as 'noupdate'."""
    file_paths = ["data/product_packaging.xml", "data/delivery_carrier.xml"]
    for file_path in file_paths:
        tools.convert.convert_file(
            cr,
            "cosanum_delivery_cosalog",
            file_path,
            None,
            mode="init",
            kind="data",
        )
