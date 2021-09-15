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
def migrate_stock_warehouse_from_cosanum_base_data(ctx):
    """Migrate 'stock.warehouse' records from 'cosanum_base_data'
    to 'cosanum_stock_warehouse'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_warehouse'
        WHERE module='cosanum_base_data'
        AND model IN ('stock.warehouse', 'res.partner')
        """
    )


@anthem.log
def migrate_stock_location_from_cosanum_base_data(ctx):
    """Migrate 'stock.location' records from 'cosanum_base_data'
    to 'cosanum_stock_location'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_location'
        WHERE module='cosanum_base_data'
        AND model IN ('stock.location', 'stock.location.storage.type')
        """
    )


@anthem.log
def pre(ctx):
    migrate_product_packaging_from_cosanum_base_data(ctx)
    migrate_stock_warehouse_from_cosanum_base_data(ctx)
    migrate_stock_location_from_cosanum_base_data(ctx)
