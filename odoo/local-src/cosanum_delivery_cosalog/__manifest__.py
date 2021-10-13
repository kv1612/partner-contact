# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "Cosanum CosaLog (rollercage)",
    "summary": "Specific rollercage handling for Cosanum",
    "version": "14.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "delivery",
        "stock",
        # OCA/product-attribute
        "product_packaging_type",
        # OCA/delivery-carrier
        "delivery_package_fee",
        # local-src
        "cosanum_product_packaging_data",
        "cosanum_delivery",
        "delivery_cosanum",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/product_packaging_type.xml",
        "data/product_packaging.xml",
        "data/delivery_carrier.xml",
        "views/product_packaging.xml",
        "views/stock_quant_package.xml",
        "reports/report_package_parcel.xml",
        "reports/reports.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": True,
}
