# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Stock Warehouse Block Auto Config',
    'summary': 'Prevent Warehouse Routes Automatic Configuration',
    'version': '12.0.1.0.0',
    'category': 'Warehouse',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'stock',
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'views/stock_warehouse_views.xml',
    ],
    'installable': False,
}
