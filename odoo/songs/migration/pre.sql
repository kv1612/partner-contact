-- Reset 'state' of ir_module_module
--
-- When we receive the database from the migration service, some addons are
-- 'to install' or 'to upgrade', set them to 'install_or_update_later'.
--
-- The goal is to allow us play all songs we need to fix data without
-- attempt to Odoo to install or update modules.
--
-- And in `pre_final.sql`, we rollback the state like it was setted previously.
--
-- With that change, in migration.yml file,
-- we need to add all modules we want to keep installed.



UPDATE
    ir_module_module
SET
    state = 'FIXME_' || state
WHERE
    state IN ('to install', 'to upgrade');

-- WARNING : the next query may be don't work with studio developments


-- Delete all action windows, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.actions.act_window';
DELETE FROM
    ir_act_window;


-- Delete all action window views, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.actions.act_window.view';
DELETE FROM
    ir_act_window_view;


-- Delete all action reports, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.actions.report';
DELETE FROM
    ir_act_report_xml;


-- Delete all report layouts, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'report.layout';
DELETE FROM
    report_layout;


-- Delete all views, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.ui.view'
AND
    res_id IN (
        SELECT
            id
        FROM
            ir_ui_view
    );

DELETE FROM
    ir_ui_view;


-- Delete all menus, will be recreated during the build.
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.ui.menu';
DELETE FROM
    ir_ui_menu;


-- Delete server_config table which broke the build and will be recreated during build
DELETE FROM
    ir_model_data
WHERE
    module = 'server_environment'
AND
    model = 'ir.model.fields'
AND
    res_id IN (SELECT id FROM ir_model_fields WHERE model = 'server.config');
DELETE FROM
    ir_model_data
WHERE
    module = 'server_environment'
AND
    model = 'ir.model'
AND
    res_id IN (SELECT id FROM ir_model WHERE model = 'server.config');
DELETE FROM
    ir_model_fields
WHERE
    model = 'server.config';
DELETE FROM
    ir_model
WHERE
    model = 'server.config';
DROP TABLE
    server_config;


-- Remove all ACL, usefull ACL will be recreated during the build
DELETE FROM
    ir_model_access;
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.model.access';


-- Remove all ir rules, usefull rules will be recreated during the build
DELETE FROM
    ir_rule;
DELETE FROM
    ir_model_data
WHERE
    model = 'ir.rule';
