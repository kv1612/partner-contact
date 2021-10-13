# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    "name": "Cosanum Account Invoicing Mode",
    "summary": "Cosanum customization for account invoicing modes.",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "author": "Camptocamp",
    "license": "AGPL-3",
    "depends": [
        # OCA/account-invoicing
        "account_invoice_mode_at_shipping",
        # OCA/stock-logistics-workflow
        "stock_picking_group_by_partner_by_carrier",
        # OCA/queue
        "queue_job",
    ],
    "website": "https://www.camptocamp.com",
    "installable": True,
}
