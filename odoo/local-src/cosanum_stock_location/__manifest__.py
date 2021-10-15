# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Location",
    "summary": "Base module hosting Cosanum stock locations",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "product_expiry",
        # OCA/stock-logistics-warehouse
        "stock_location_bin_name",
        "stock_location_position",
        "stock_location_tray",
        "stock_location_zone",
        # OCA/wms
        "stock_storage_type",
        "stock_storage_type_putaway_abc",
        # local-src
        "cosanum_stock_warehouse",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_location_storage_type.xml",
        "data/stock_location_tray_type.xml",
        "data/stock_location.xml",
    ],
    "installable": True,
}
