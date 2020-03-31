# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Account financial report salesperson',
    'summary': 'Inprove OCA account financial report with the salesperson',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        # OCA
        'account_financial_report',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'wizard/aged_partner_balance_wizard.xml',
        'wizard/open_items_wizard.xml',
    ],
    'installable': True,
}
