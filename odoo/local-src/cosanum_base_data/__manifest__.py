# Copyright 2019 Camptocamp SA
{
    # NOTE: IMPORTANT. This module contains only *DATA*
    'name': 'Cosanum Base Data',
    # see
    # https://confluence.camptocamp.com/confluence/display/BS/Structure+of+local+addons+in+a+project
    # it does not have any dependency on other local addons. It must contain
    # what will be shared by several Cosanum_xx addons, cross-feature
    # fields (eg: a field on the company), mainly data files.
    'summary': 'Base *data* used in other Cosanum addons',
    'version': '13.0.1.0.0',
    'category': 'Hidden',
    'author': 'Camptocamp',
    # NOTE: IMPORTANT. This module contains only *DATA*
    # Then, the license we put is irrelevant as it doesn't
    # apply on data (see BSCOS-1873)
    'license': 'LGPL-3',
    'depends': [
        'base',
        'delivery',
        'mrp',
        'purchase_stock',
        'mrp_subcontracting',
        # odoo/local-src
        'delivery_brauch',
        'stock_warehouse_block_auto_config',
        # from odoo/external-src/sale-workflow
        'sale_by_packaging',
        'sale_order_line_packaging_qty',
        'sale_stock_mto_as_mts_orderpoint',
        # from odoo/external-src/stock-logistics-workflow
        'stock_picking_group_by_partner_by_carrier',
        'stock_putaway_by_route',
        'stock_picking_backorder_strategy',
        # from odoo/external-src/stock-logistics-warehouse
        'stock_location_bin_name',
        'stock_location_zone',
        'stock_dynamic_routing',
        'stock_vertical_lift_storage_type',
        'stock_vertical_lift_kardex',
        'stock_reserve_rule',
        'stock_picking_consolidation_priority',
        'stock_picking_completion_info',
        'stock_available_to_promise_release',
        'product_packaging_type_required',
        'stock_orderpoint_route',
        'stock_orderpoint_move_link',
        'stock_checkout_sync',
        'procurement_auto_create_group',

        # from odoo/external-src/server-env
        'server_environment_delivery',

        # from odoo/external-src/delivery-carrier
        'delivery_carrier_pricelist',
        'delivery_postlogistics',

        # from odoo/external-src/wms
        'stock_picking_type_shipping_policy',
        'stock_move_source_relocate',
        'delivery_carrier_preference',
        'delivery_carrier_warehouse',
        'stock_storage_type_buffer',
        'stock_storage_type_putaway_abc',

        # from odoo/external-src/product-attribute
        'product_packaging_type_pallet',

        # from odoo/src
        'product_expiry',
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'data/stock_warehouse_data.xml',
        'data/picking_type_sequence_data.xml',
        'data/stock_location_storage_type_data.xml',
        'data/stock_location_tray_type.xml',
        'data/stock_package_storage_type_data.xml',
        'data/stock_location_data.xml',
        'data/stock_picking_type_data.xml',
        'data/HRL_stock_picking_type_data.xml',
        'data/stock_location_route.xml',
        'data/stock_rule.xml',
        'data/product_packaging_type_data.xml',
        'data/stock_putaway_rule_data.xml',
        "data/product_packaging.xml",
        "data/postlogistics_license.xml",
        'data/delivery_carrier_data.xml',
        'data/stock_reserve_rule_data.xml',
        'data/stock_reserve_rule_removal_data.xml',
        'data/stock_routing_data.xml',
        'data/stock_source_relocate_data.xml',
        'data/stock_storage_location_sequence_data.xml',
        'data/vertical_lift_shuttle_data.xml',
        'data/delivery_carrier_preference_data.xml',
        'data/stock_storage_location_buffer_data.xml',
        # Data
        "data/res.lang.csv",
    ],
    'installable': True,
}
