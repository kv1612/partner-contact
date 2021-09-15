# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Picking Backorder Strategy",
    "summary": "Cosanum integration of Backorder Strategy",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/stock-logistics-workflow
        "stock_picking_backorder_strategy",
        # local-src
        "cosanum_stock_picking_type",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_picking_type.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": True,
}
