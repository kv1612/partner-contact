# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

import anthem


@anthem.log
def disable_shopinvader_partner_email_constraint(ctx):
    # Disable the unicity constraint on partner emails brought by Shopinvader.
    # This constraint is blocking the installation of 'cosanum_stock_warehouse'
    # because there are ~4 partners with the same email in the DB
    # (werrikon@cosanum.ch). Maybe other partners are impacted by this check,
    # so better to disable this constraint during the migration, it'll be
    # re-enable in the 'post' step.
    ctx.env["ir.config_parameter"].set_param(
        "shopinvader.no_partner_duplicate", "False"
    )


@anthem.log
def enable_shopinvader_partner_email_constraint(ctx):
    ctx.env["ir.config_parameter"].set_param(
        "shopinvader.no_partner_duplicate", "True"
    )


@anthem.log
def pre(ctx):
    disable_shopinvader_partner_email_constraint(ctx)


@anthem.log
def post(ctx):
    enable_shopinvader_partner_email_constraint(ctx)
