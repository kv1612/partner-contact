# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Reserve Rule",
    "summary": "Base module hosting Cosanum stock reserve rules",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/stock-logistics-warehouse
        "stock_reserve_rule",
        # local-src
        "cosanum_product_packaging",
        "cosanum_stock_location",
        "cosanum_stock_picking_type",
        "cosanum_stock_warehouse",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_reserve_rule.xml",
        "data/stock_reserve_rule_removal.xml",
    ],
    "installable": True,
}
