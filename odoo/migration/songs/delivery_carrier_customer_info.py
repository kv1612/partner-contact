# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import anthem
from openupgradelib import openupgrade


def migrate_cosanum_delivery_to_delivery_carrier_customer_info(ctx):
    """Migrate data from 'cosanum_delivery' to the new OCA module
    'delivery_carrier_customer_info'.
    """
    # By moving existing XML-IDs to the new addon before the install/update
    # step, this prevents Odoo to remove underlying data.
    xml_ids = [
        # model
        "model_res_partner",
        "model_res_partner_delivery_info",
        # fields
        "field_res_partner__delivery_info_id",
        "field_res_partner_delivery_info____last_update",
        "field_res_partner_delivery_info__active",
        "field_res_partner_delivery_info__create_date",
        "field_res_partner_delivery_info__create_uid",
        "field_res_partner_delivery_info__display_name",
        "field_res_partner_delivery_info__id",
        "field_res_partner_delivery_info__name",
        "field_res_partner_delivery_info__text",
        "field_res_partner_delivery_info__write_date",
        "field_res_partner_delivery_info__write_uid",
        "field_res_users__delivery_info_id",
        "field_shopinvader_partner__delivery_info_id",
    ]
    xmlids_spec = [
        (
            f"cosanum_delivery.{xml_id}",
            f"delivery_carrier_customer_info.{xml_id}",
        )
        for xml_id in xml_ids
    ]
    openupgrade.rename_xmlids(ctx.env.cr, xmlids_spec)


@anthem.log
def pre(ctx):
    migrate_cosanum_delivery_to_delivery_carrier_customer_info(ctx)
