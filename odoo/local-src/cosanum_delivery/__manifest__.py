# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Cosanum Delivery",
    "summary": "Cosanum customization for Delivery module",
    "version": "13.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["cosanum_base", "delivery", "sale_partner_delivery_window"],
    "data": ["views/res_partner.xml"],
}
