# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Cosanum Delivery Brauch",
    "summary": "Cosanum customization for Delivery Brauch module",
    "version": "14.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # OCA/delivery-carrier
        "server_environment_delivery",
        # OCA/stock-logistics-workflow
        "stock_partner_delivery_window",
        # OCA/sale-workflow
        "sale_delivery_date",
        # local-src
        "cosanum_delivery",
        "cosanum_delivery_data",
        "cosanum_product_packaging_data",
        "cosanum_stock_warehouse",
        "delivery_brauch",
    ],
    "data": [
        "data/delivery_carrier.xml",
        "data/product_packaging.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
}
