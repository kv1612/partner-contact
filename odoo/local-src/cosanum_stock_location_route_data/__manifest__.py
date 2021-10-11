# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Route",
    "summary": "Base module hosting Cosanum stock routes",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "stock",
        # OCA/wms
        "stock_available_to_promise_release",
        "delivery_carrier_preference",
        # local-src
        "cosanum_stock_warehouse_data",
        "cosanum_stock_picking_type_data",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_location_route.xml",
    ],
    "installable": True,
}
