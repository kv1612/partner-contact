# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Warehouse (Block Auto Config)",
    "summary": "Cosanum stock warehouse (block automatic configuration)",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # local-src
        "cosanum_stock_warehouse",
        "stock_warehouse_block_auto_config"   # TODO to migrate
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_warehouse.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": False,
}