# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Product logistics UoM",
    "summary": "Cosanum integration of Product logistics UoM",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/product-attribute
        "product_logistics_uom",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/uom_uom.xml",
        "data/ir_config_parameter.xml",
    ],
    "installable": True,
}
