# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Picking Type",
    "summary": "Base module hosting Cosanum stock picking types",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "stock",
        # OCA/wms
        "stock_picking_completion_info",
        "stock_picking_type_shipping_policy",
        # local-src
        "cosanum_stock_warehouse",
        "cosanum_stock_location_data",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_picking_type_sequence.xml",
        "data/stock_picking_type.xml",
        "data/HRL_stock_picking_type.xml",
    ],
    "installable": True,
}
