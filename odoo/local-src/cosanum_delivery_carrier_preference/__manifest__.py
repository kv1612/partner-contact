# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Cosanum Delivery Carrier Preference",
    "summary": "Cosanum integration of Delivery Carrier Preference",
    "version": "14.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # OCA/wms
        "delivery_carrier_preference",
        # local-src
        "cosanum_delivery_data",
    ],
    "data": [
        "data/delivery_carrier_preference.xml",
    ],
}
