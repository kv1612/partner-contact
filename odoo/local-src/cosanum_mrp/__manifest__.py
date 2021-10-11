# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum MRP",
    "summary": "Cosanum MRP integration",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "mrp",
        # local-src
        "cosanum_stock_warehouse_data",
        "cosanum_stock_picking_type_data",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_warehouse.xml",
        "data/stock_location_route.xml",
        "data/stock_picking_type.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": True,
}
