# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import anthem


@anthem.log
def migrate_res_groups_from_cosanum_base(ctx):
    """Migrate 'res.groups' records from 'cosanum_base' to 'cosanum_purchase_stock'."""
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_purchase_stock'
        WHERE module='cosanum_base'
        AND model='res.groups'
        """
    )


@anthem.log
def pre(ctx):
    migrate_res_groups_from_cosanum_base(ctx)
