# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Pricelist partner group",
    "summary": "Saves unit prices in the pricelist for future orders",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        "partner_company_group",
        "product",
        "sale",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        # views
        "views/product_pricelist.xml",
        "views/res_partner.xml",
        # wizards
        "wizards/res_config_settings.xml",
    ],
    "installable": True,
}
