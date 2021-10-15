# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Delivery Carrier (SwissPost)",
    "summary": "Base module hosting Cosanum delivery carriers (SwissPost)",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # local-src
        # "delivery_postlogistics", # TODO to migrate
        "cosanum_product_packaging",
        # "cosanum_delivery_carrier",   # TODO
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/product_packaging.xml",
        # "data/delivery_carrier.xml",  # TODO
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": False,
}
