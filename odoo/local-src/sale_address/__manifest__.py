# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Sale Addresses',
    'summary': 'Add default shipping and invoice addresses on sales orders',
    'version': '12.0.1.0.0',
    'category': 'Hidden',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'sale'
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'views/contact_view.xml'
    ],
    'installable': False,
}
