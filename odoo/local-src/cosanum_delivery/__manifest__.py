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
        # OCA/delivery-carrier
        "delivery_carrier_customer_info",
        # OCA/sale-workflow
        # "sale_partner_delivery_window",   # TODO to migrate
        # local-src
        "cosanum_delivery_data",
    ],
    "data": [
        "views/res_partner.xml",
        "views/packaging_views.xml",
    ],
}
