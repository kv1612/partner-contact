# -*- coding: utf-8 -*-
# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Cosanum HR',
    'summary': 'Specific HR for Cosanum',
    'version': '12.0.1.0.0',
    'category': 'HR',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'hr',
        'hr_attendance',
        'hr_holidays',
    ],
    'website': 'http://www.camptocamp.com',
    'data': [
        'views/hr_attendance_views.xml',
        'views/hr_holidays_views.xml',
    ],
    'installable': True,
}
