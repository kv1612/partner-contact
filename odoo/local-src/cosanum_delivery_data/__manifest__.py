# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Delivery Carrier",
    "summary": "Base module hosting Cosanum delivery carriers",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "stock",
        "delivery",
        # OCA/delivery-carrier
        "delivery_carrier_pricelist",
        "delivery_package_fee",
        "server_environment_delivery",
        # OCA/wms
        "delivery_carrier_warehouse",
        # local-src
        "cosanum_product_packaging_data",
        "cosanum_stock_warehouse",
        "cosanum_stock_picking_type",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/product_product.xml",
        "data/delivery_carrier.xml",
    ],
    "installable": True,
}
