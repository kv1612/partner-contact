# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import anthem


@anthem.log
def migrate_product_packaging_from_cosanum_base_data(ctx):
    """Migrate 'product.packaging' records from 'cosanum_base_data'
    to 'cosanum_product_packaging'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_product_packaging'
        WHERE module='cosanum_base_data'
        AND model='product.packaging'
        """
    )


@anthem.log
def pre(ctx):
    migrate_product_packaging_from_cosanum_base_data(ctx)
