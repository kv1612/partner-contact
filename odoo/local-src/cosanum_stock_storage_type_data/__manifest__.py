# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Stock Storage Type",
    "summary": "Base module hosting Cosanum stock storage types",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/wms
        "stock_storage_type",
        "stock_storage_type_buffer",
        # local-src
        "cosanum_stock_location_data",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/stock_package_storage_type.xml",
        "data/stock_storage_location_sequence.xml",
        "data/stock_location_storage_buffer.xml",
    ],
    "installable": True,
}
