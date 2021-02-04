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
