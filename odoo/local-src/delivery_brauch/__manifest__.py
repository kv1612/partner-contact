# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Delivery Brauch",
    "summary": "Send your shipping to Brauch Transporte",
    "version": "14.0.1.0.0",
    "category": "Operations/Inventory/Delivery",
    "website": "https://github.com/OCA/delivery-carrier",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["delivery", "queue_job", "server_environment"],
    "data": [
        "data/queue_job_channel.xml",
        "data/queue_job_function.xml",
        "data/res_lang.xml",
        "views/delivery.xml",
        "views/res_partner.xml",
        "views/stock_picking.xml",
    ],
}
