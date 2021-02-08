# Copyright 2021 Camptocamp SA (https://www.camptocamp.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
import os

from openupgradelib import openupgrade  # pylint: disable=W7936


@openupgrade.migrate()
def migrate(env, version):
    # In Odoo V13, removing a column from the model drops the corresponding
    # table from the database, even if it has data. So we are combining
    # a pre- and post-migration. The pre-migration copies the column to be
    # removed, delivery_info, into the temporary column delivery_info_tmp.
    # Then, this post-migration takes the value stored there to create records
    # of the new model res.partner.delivery.info, and once they have been
    # created, the temporary column is removed at the end.
    #
    # The move between delivery_info_tmp to the newly created records of
    # the model res.partner.delivery.info is intended to be done as follows:
    #     1) Creates as many records of the type res.partner.delivery.info
    #        as different messages are in the temporal column delivery_info_tmp
    #        in a res.partner.
    #            The new model has two fields, name and text. Field text
    #        contains all the content of delivery_info_tmp, while the field
    #        name contains only its first line.
    #     2) For every partner that is active, assigns the record created
    #        before. So different partners sharing the same message will
    #        share the same record.
    #
    # This is done efficiently: iterates over partners and, if the text is
    # already stored in a record of res.partner.delivery.info, links to it;
    # otherwise creates it, and then links to it.

    if not version:
        return

    res_partner_delivery_info = env["res.partner.delivery.info"]
    res_partner = env["res.partner"]

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

    openupgrade.drop_columns(env.cr, [("res_partner", "delivery_info_tmp")])
