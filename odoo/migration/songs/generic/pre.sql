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
