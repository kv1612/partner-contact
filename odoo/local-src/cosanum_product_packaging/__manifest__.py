# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Product Packaging",
    "summary": "Base module hosting Cosanum product packaging",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # core
        "product",
        # OCA/product-attribute
        "product_packaging_type",
        "product_packaging_type_required",
        "product_packaging_type_pallet",
        # OCA/sale-workflow
        "sale_by_packaging",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/product_packaging_type.xml",
        "data/product_packaging.xml",
    ],
    "installable": True,
}
