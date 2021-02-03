# Copyright 2021 Camptocamp SA (https://www.camptocamp.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
import hashlib
import os

from openupgradelib import openupgrade  # pylint: disable=W7936


@openupgrade.migrate()
def migrate(env, version):
    if not version:
        return

    res_partner_delivery_info = env["res.partner.delivery.info"]
    res_partner = env["res.partner"]
    ir_model_data = env["ir.model.data"]

    env.cr.execute(
        """
        SELECT id, COALESCE(delivery_info_tmp, '') AS delivery_info_old
        FROM res_partner
        WHERE active = TRUE;
        """
    )

    for row in env.cr.dictfetchall():
        partner_id = int(row["id"])
        delivery_info_full = row["delivery_info_old"].strip()
        if delivery_info_full:
            partner = res_partner.browse(partner_id)

            # We assume the name is the first line, if there are several.
            linesep_pos = delivery_info_full.find(os.linesep)
            if linesep_pos == -1:
                delivery_info_name = delivery_info_full
            else:
                delivery_info_name = delivery_info_full[:linesep_pos]

            # If a record already exists, assign it; otherwise: create and assign.
            delivery_info_record = res_partner_delivery_info.search(
                [
                    ("name", "=", delivery_info_name),
                    ("text", "=", delivery_info_full),
                ],
                limit=1,
            )
            if delivery_info_record:
                partner.delivery_info_id = delivery_info_record
            else:
                delivery_info_record = res_partner_delivery_info.create(
                    {"name": delivery_info_name, "text": delivery_info_full}
                )
                partner.delivery_info_id = delivery_info_record
                xml_id_prefix = "cosanum_delivery.res_partner_delivery_info_"
                xml_id_hash = hashlib.md5(
                    delivery_info_full.encode("utf-8")
                ).hexdigest()
                ir_model_data._update_xmlids(
                    [
                        {
                            "xml_id": "{}_{}".format(
                                xml_id_prefix, xml_id_hash
                            ),
                            "record": delivery_info_record,
                            "noupdate": True,
                        }
                    ]
                )
    openupgrade.drop_columns(env.cr, [("res_partner", "delivery_info_tmp")])
