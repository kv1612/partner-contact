# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from time import gmtime, strftime

import anthem

UNINSTALL_MODULES_LIST = [
    # Here we need to list:
    # all modules installed in previous version of odoo,
    # but we don't want to keep.
    # ===> Modules core/enterprise we don't want
    # ===> Modules OCA we don't want
    # OCA/example-1
    # OCA/example-2
    # ===> Specific modules we don't want
    # ===> OCA modules not available yet, but we want
    # OCA/example-1
    # OCA/example-2
    # ===> Specific modules not migrated yet, but we want
    # ===> OCA modules not available yet, but we don't know if we want
    # OCA/example-1
    # OCA/example-2
    # ===> Specific modules not migrated yet, but we don't know if we want
    # ===> Modules unavailable not installed, but we still have metadata
    # oca/account-financial-tools
    'account_financial_discount',
    # oca/account-invoice-reporting
    'account_invoice_line_sale_line_position',
    # oca/account-closing
    'account_cutoff_accrual_base',
    'account_cutoff_accrual_dates',
    'account_cutoff_prepaid',
    'account_multicurrency_revaluation',
    # oca/account-reconcile
    'account_partner_reconcile',
    'account_reconcile_model_strict_match_amount',
    'account_reconcile_restrict_partner_mismatch',
    # oca/bank-statement-import
    'account_bank_statement_import_camt_oca',
    'account_bank_statement_import_oca_camt54',
    'account_bank_statement_import_transfer_move',
    # oca/community-data-files
    'l10n_eu_product_adr',
    # oca/delivery-carrier
    'delivery_postlogistics',
    'delivery_postlogistics_dangerous_goods',
    'delivery_postlogistics_server_env',
    'delivery_send_to_shipper_at_operation',
    'server_environment_delivery',
    # oca/edi
    'account_e-invoice_generate',
    'account_invoice_export',
    'account_invoice_export_server_env',
    'account_invoice_ubl',
    'base_ebill_payment_contract',
    'sale_order_customer_free_ref',
    'sale_order_import_ubl_customer_free_ref',
    'sale_order_import_ubl_http',
    # oca/l10n-switzerland
    'ebill_paynet',
    'ebill_paynet_account_financial_discount',
    'ebill_paynet_customer_free_ref',
    'l10n_ch_invoice_reports',
    'l10n_ch_isr_payment_grouping',
    'l10n_ch_isrb',
    'server_env_ebill_paynet',
    # oca/product-attribute
    'product_packaging_unit_price_calculator',
    # oca/product-variant
    'product_variant_change_attribute_value',
    # oca/purchase-workflow
    'vendor_transport_lead_time',
    # oca/queue
    'queue_job_subscribe',
    # oca/sale-workflow
    'sale_cutoff_time_delivery',
    'sale_order_line_replacement',
    'sale_partner_cutoff_delivery_window',
    'sale_partner_delivery_window',
    'sale_product_set_sale_by_packaging',
    # oca/stock-logistics-reporting
    'stock_picking_group_by_partner_by_carrier_sale_line_position',
    # oca/stock-logistics-workflow
    'delivery_total_weight_from_packaging',
    'sale_stock_mto_as_mts_orderpoint',
    'stock_dangerous_goods',
    'stock_lock_lot',
    'stock_partner_delivery_window',
    'stock_picking_group_by_partner_by_carrier_by_date',
    # oca/stock-logistics-warehouse
    'stock_move_auto_assign',
    'stock_vertical_lift_empty_tray_check',
    'stock_vertical_lift_packaging_type',
    'stock_vertical_lift_qty_by_packaging',
    # oca/wms
    'delivery_preference_glue_stock_picking_group',
    'sale_stock_available_to_promise_release_cutoff',
    'sale_stock_available_to_promise_release_dropshipping',
    'shopfloor_dangerous_goods',
    'shopfloor_dangerous_goods_mobile',
    'shopfloor_delivery_shipment',
    'shopfloor_delivery_shipment_mobile',
    'shopfloor_rest_log',
    'stock_dynamic_routing_checkout_sync',
    'stock_reception_screen_measuring_device',
    'stock_reception_screen_mrp_subcontracting',
    'stock_reception_screen_qty_by_packaging',
    # shopinvader/odoo-shopinvader
    'shopinvader_customer_price_wishlist',
    'shopinvader_delivery_state',
    'shopinvader_portal_mode',
    'shopinvader_product_template_multi_link_date_span',
    'shopinvader_product_variant_multi_link',
    'shopinvader_sale_packaging',
    'shopinvader_sale_packaging_wishlist',
    # camptocamp/odoo-enterprise-addons
    'account_followup_communication_override',
    'account_followup_partner_query_materialized',
    'account_followup_specific_address',
    'account_sepa_l10n_ch',
    # camptocamp/wms-workload
    'shopfloor_kanban',
    'stock_picking_type_kanban',
    'stock_release_channel',
    'stock_release_channel_ddmrp',
    # forgeflow/ddmrp-professional
    'ddmrp_simulation',
    # forgeflow/forecasting
    'forecast_base',
    'forecast_fbprophet',
    'forecast_stock',
    # local-src
    'account_financial_report_salesperson',
    'account_invoice_line_migel_number',
    'account_invoice_mode_monthly_report',
    'account_invoice_qr_report',
    'account_invoice_summary',
    'account_invoice_summary_delivery_address',
    'account_invoice_summary_migel_number',
    'cosanum_account',
    'cosanum_account_bank_statement_import_camt54',
    'cosanum_account_invoice_export',
    'cosanum_account_invoice_mode',
    'cosanum_account_move_tier_validation',
    'cosanum_account_payment_mode',
    'cosanum_account_sale',
    'cosanum_base',
    'cosanum_base_data',
    'cosanum_contact',
    'cosanum_crm',
    'cosanum_ddmrp',
    'cosanum_ddmrp_chatter',
    'cosanum_delivery',
    'cosanum_delivery_brauch',
    'cosanum_delivery_carrier_preference',
    'cosanum_delivery_cosalog',
    'cosanum_delivery_cosalog_brauch',
    'cosanum_delivery_dhl',
    'cosanum_delivery_postlogistics',
    'cosanum_followup_report',
    'cosanum_helpdesk',
    'cosanum_hr',
    'cosanum_importer',
    'cosanum_kardex',
    'cosanum_knowledge',
    'cosanum_l10n_eu_product_adr',
    'cosanum_management_system',
    'cosanum_product',
    'cosanum_product_medical',
    'cosanum_product_multi_link',
    'cosanum_product_packaging_dimension',
    'cosanum_purchase',
    'cosanum_purchase_propagate_qty',
    'cosanum_purchase_report',
    'cosanum_release_channel',
    'cosanum_report',
    'cosanum_report_auto_print',
    'cosanum_report_invoice',
    'cosanum_sale',
    'cosanum_sale_exception',
    'cosanum_sale_exception_drug_legitimacy',
    'cosanum_sale_exception_partner_archived',
    'cosanum_sale_exception_procurement_legitimacy_carrier',
    'cosanum_sale_exception_product_archived',
    'cosanum_sale_exception_product_discontinued',
    'cosanum_sale_product_medical',
    'cosanum_security',
    'cosanum_shipment_advice_cosalog',
    'cosanum_shop_backend',
    'cosanum_shop_import_media',
    'cosanum_shop_notification',
    'cosanum_shop_pricelist',
    'cosanum_shop_product',
    'cosanum_shop_sale_packaging',
    'cosanum_shop_sale_replacement',
    'cosanum_shop_storage_media',
    'cosanum_shop_target_market',
    'cosanum_shopfloor',
    'cosanum_spitex',
    'cosanum_stock',
    'cosanum_stock_measuring_device_zippcube',
    'cosanum_stock_picking_group_by_partner_by_carrier',
    'cosanum_target_market',
    'cosanum_translation',
    'ddmrp_priority',
    'ddmrp_sale_exclude_from_adu',
    'delivery_dhl_archive_doc',
    'delivery_dhl_server_env',
    'delivery_send_to_shipper_at_operation_brauch',
    'dhl_default_printer',
    'ebill_medidata',
    'ebill_medidata_export',
    'forecasting_sale_history',
    'l10n_ch_adr_report',
    'mail_server_amazon_ses',
    'mrp_subcontracting_without_tracking',
    'partner_title_order',
    'postlogistics_default_printer',
    'pricelist_cache',
    'pricelist_cache_partner_group',
    'pricelist_cache_product_manufactured_for',
    'pricelist_cache_rest',
    'pricelist_partner_group',
    'product_conformity',
    'product_pricelist_code',
    'product_pricelist_default',
    'product_sale_manufactured_for',
    'product_set_sale_manufactured_for',
    'product_status',
    'purchase_incoterm',
    'sale_address',
    'sale_exception_product_sale_manufactured_for',
    'sale_order_import_spitex',
    'sale_order_import_ubl_http_ortho',
    'shopinvader_customer_special_product',
    'web_enterprise_m2x_options',
    'web_generate_assets',
]


@anthem.log
def update_state_for_uninstalled_modules(ctx):
    """ Update state for uninstalled modules
    to avoid to install/update them into the build """
    if UNINSTALL_MODULES_LIST:
        sql = """
            UPDATE
                ir_module_module
            SET
                state = 'uninstalled'
            WHERE
                name IN %s;
        """
        ctx.env.cr.execute(sql, [tuple(UNINSTALL_MODULES_LIST)])
    else:
        ctx.log_line("No modules to uninstall")


@anthem.log
def uninstall_modules(ctx):
    """ Uninstall modules """
    if UNINSTALL_MODULES_LIST:
        # Depending on the project the un-installation of all modules in one
        # call can imply un-installation errors (and then, build failure).
        # We uninstall modules one by one
        # to have less possible failures when migration build.
        # This way we also ee which modules take more time to uninstall.

        for module_name in UNINSTALL_MODULES_LIST:
            ctx.log_line(
                "%s Try to uninstall module: %s"
                % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), module_name)
            )

            module = ctx.env['ir.module.module'].search(
                [('name', '=', module_name)]
            )
            if module:
                # Odoo add a check to deny uninstall of non-installed module.
                # But in migration context,
                # we want to uninstall module without have an installed status.
                # Because for some modules, we don't have sources.
                #
                # Then we copy/paste here a part of code core module
                # to uninstall manually module.
                deps = module.downstream_dependencies()
                if deps:
                    ctx.log_line(
                        "====> Module with dependency to uninstall: {}".format(
                            deps.mapped('name')
                        )
                    )
                (module + deps).write({'state': 'to remove'})

                module._button_immediate_function(function=lambda x: {})
            else:
                ctx.log_line("====> Module not found")
    else:
        ctx.log_line("No modules to uninstall")


@anthem.log
def pre(ctx):
    """ PRE: uninstall """
    update_state_for_uninstalled_modules(ctx)


@anthem.log
def post(ctx):
    """ POST: uninstall """
    uninstall_modules(ctx)
