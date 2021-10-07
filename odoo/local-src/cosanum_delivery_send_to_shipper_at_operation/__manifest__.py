# Copyright 2019-2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cosanum Delivery Send To Shipper at Operation",
    "summary": "Cosanum integration of 'delivery_send_to_shipper_at_operation'.",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/delivery-carrier
        "delivery_send_to_shipper_at_operation",
        # local-src
        "cosanum_delivery_data",
    ],
    "website": "https://www.camptocamp.com",
    "data": [
        "data/delivery_carrier.xml",
    ],
    # NOTE: as original records are flagged with 'noupdate', the only way to get
    # them updated is to read the XML data file manually when the module is installed
    "post_init_hook": "update_data",
    "installable": True,
}
