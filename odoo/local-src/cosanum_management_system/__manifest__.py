# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Cosanum Management System',
    'summary': 'Specific Management System for Cosanum',
    'version': '13.0.1.0.0',
    'category': 'Management System',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'document_page_procedure',
        'document_page_work_instruction',
        'mgmtsystem',
        'mgmtsystem_manual',
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'views/menus.xml'
    ],
    'installable': True,
}
