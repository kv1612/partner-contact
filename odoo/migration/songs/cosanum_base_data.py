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
    # Flag the new module 'cosanum_product_packaging' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_product_packaging'
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
    # Flag the new module 'cosanum_stock_warehouse' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_warehouse'
        """
    )


@anthem.log
def migrate_stock_location_from_cosanum_base_data(ctx):
    """Migrate 'stock.location' records from 'cosanum_base_data'
    to 'cosanum_stock_location_data'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_location_data'
        WHERE module='cosanum_base_data'
        AND model IN ('stock.location', 'stock.location.storage.type')
        """
    )
    # Flag the new module 'cosanum_stock_warehouse' as installed to
    #   - avoid overwritting existing configuration data
    #   - greatly improve migration speed (~30min of recomputation of 30k
    #     locations in the database)
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_location_data'
        """
    )


@anthem.log
def migrate_stock_picking_type_from_cosanum_base_data(ctx):
    """Migrate 'stock.picking.type' records from 'cosanum_base_data'
    to 'cosanum_stock_picking_type'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_picking_type'
        WHERE module='cosanum_base_data'
        AND model IN ('stock.picking.type', 'ir.sequence')
        """
    )
    # Flag the new module 'cosanum_stock_picking_type' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_picking_type'
        """
    )


@anthem.log
def migrate_stock_location_route_from_cosanum_base_data(ctx):
    """Migrate 'stock.location.route' records from 'cosanum_base_data'
    to 'cosanum_stock_location_route'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_location_route'
        WHERE module='cosanum_base_data'
        AND model = 'stock.location.route'
        """
    )
    # Flag the new module 'cosanum_stock_location_route' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_location_route'
        """
    )


def migrate_delivery_carrier_from_cosanum_base_data(ctx):
    """Migrate 'delivery.carrier' records from 'cosanum_base_data'
    to 'cosanum_delivery_data'.
    """
    # The only 'product.product' records were delivery fee related to
    # 'cosanum_base_data'
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_delivery_data'
        WHERE module='cosanum_base_data'
        AND model IN ('delivery.carrier', 'product.product')
        """
    )
    # Flag the new module 'cosanum_delivery_data' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_delivery_data'
        """
    )


@anthem.log
def pre(ctx):
    migrate_product_packaging_from_cosanum_base_data(ctx)
    migrate_stock_warehouse_from_cosanum_base_data(ctx)
    migrate_stock_location_from_cosanum_base_data(ctx)
    migrate_stock_picking_type_from_cosanum_base_data(ctx)
    migrate_stock_location_route_from_cosanum_base_data(ctx)
    migrate_delivery_carrier_from_cosanum_base_data(ctx)
