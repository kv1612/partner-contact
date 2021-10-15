# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Cosanum Delivery",
    "summary": "Cosanum customization for Delivery module",
    "version": "14.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # core
        "delivery",
        "sales_team",
        "stock",
        # OCA/delivery-carrier
        "delivery_carrier_customer_info",
        "delivery_carrier_pricelist",
        "delivery_package_fee",
        "server_environment_delivery",
        # OCA/sale-workflow
        # "sale_partner_delivery_window",   # TODO to migrate
        # OCA/wms
        "delivery_carrier_warehouse",
        # local-src
        "cosanum_product_packaging",
        "cosanum_stock_warehouse",
        "cosanum_stock_picking_type",
    ],
    "data": [
        "data/product_product.xml",
        "data/delivery_carrier.xml",
        "views/res_partner.xml",
        "views/packaging_views.xml",
    ],
}
