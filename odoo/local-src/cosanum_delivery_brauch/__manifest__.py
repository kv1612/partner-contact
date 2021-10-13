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
        "cosanum_stock_warehouse_data",
        "cosanum_delivery",
        "delivery_brauch",
    ],
    "data": [],
}
