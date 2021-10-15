# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Putaway Rule",
    "summary": "Base module hosting Cosanum stock putaway rules",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "mrp",
        "purchase_stock",
        "stock",
        # local-src
        "cosanum_stock_warehouse",
        "cosanum_stock_location",
        "cosanum_stock_location_route",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_putaway_rule.xml",
    ],
    "installable": True,
}
