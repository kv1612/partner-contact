# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Warehouse",
    "summary": "Base module hosting Cosanum stock warehouse",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "stock",
        "mrp",
        "mrp_subcontracting",
        "purchase_stock",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_warehouse.xml",
    ],
    "installable": True,
}
