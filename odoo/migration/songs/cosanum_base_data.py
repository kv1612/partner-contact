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
    to 'cosanum_stock_location'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_location'
        WHERE module='cosanum_base_data'
        AND model IN (
            'stock.location',
            'stock.location.storage.type',
            'stock.location.tray.type',
            'stock.package.storage.type',
            'stock.storage.location.sequence',
            'stock.location.storage.buffer'
        )
        """
    )
    # Flag the new module 'cosanum_stock_location' as installed to
    #   - avoid overwritting existing configuration data
    #   - greatly improve migration speed (~30min of recomputation of 30k
    #     locations in the database)
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_location'
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
    to 'cosanum_delivery'.
    """
    # The only 'product.product' records were delivery fee related to
    # 'cosanum_base_data'
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_delivery'
        WHERE module='cosanum_base_data'
        AND model IN ('delivery.carrier', 'product.product')
        """
    )
    # Flag the new module 'cosanum_delivery' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_delivery'
        """
    )


def migrate_delivery_carrier_preference_from_cosanum_base_data(ctx):
    """Migrate delivery carrier preferences records from 'cosanum_base_data'
    to 'cosanum_delivery_carrier_preference'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_delivery_carrier_preference'
        WHERE module='cosanum_base_data'
        AND model = 'delivery.carrier.preference'
        """
    )


def migrate_stock_putaway_rule_from_cosanum_base_data(ctx):
    """Migrate putaway rule records from 'cosanum_base_data'
    to 'cosanum_stock_putaway_rule'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_putaway_rule'
        WHERE module='cosanum_base_data'
        AND model = 'stock.putaway.rule'
        """
    )
    # Flag the new module 'cosanum_stock_putaway_rule' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_putaway_rule'
        """
    )


def migrate_stock_reserve_rule_from_cosanum_base_data(ctx):
    """Migrate reserve_rule records from 'cosanum_base_data'
    to 'cosanum_stock_reserve_rule'.
    """
    ctx.env.cr.execute(
        """
        UPDATE ir_model_data
        SET module='cosanum_stock_reserve_rule'
        WHERE module='cosanum_base_data'
        AND model IN (
            'stock.reserve.rule',
            'stock.reserve.rule.removal'
        )
        """
    )
    # Flag the new module 'cosanum_stock_reserve_rule' as installed to avoid
    # overwritting existing configuration data
    ctx.env.cr.execute(
        """
        UPDATE ir_module_module SET state='installed'
        WHERE name='cosanum_stock_reserve_rule'
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
    migrate_delivery_carrier_preference_from_cosanum_base_data(ctx)
    migrate_stock_putaway_rule_from_cosanum_base_data(ctx)
    migrate_stock_reserve_rule_from_cosanum_base_data(ctx)
