# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import anthem
from openupgradelib.openupgrade import update_module_names


@anthem.log
def rename_modules(ctx):
    update_module_names(
        ctx.env.cr,
        [('account_e-invoice_generate', 'account_einvoice_generate')],
        merge_modules=True,
    )


@anthem.log
def pre(ctx):
    rename_modules(ctx)
