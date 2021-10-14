# Copyright 2019-2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Cosanum Base',
    # see
    # https://confluence.camptocamp.com/confluence/display/BS/Structure+of+local+addons+in+a+project
    # it does not have any dependency on other local addons. It must contain
    # what will be shared by several Cosanum_xx addons, cross-feature
    # fields (eg: a field on the company).
    'summary': 'Base code shared with all cosanum_* modules',
    'version': '13.0.1.0.0',
    'category': 'Hidden',
    'author': 'Camptocamp',
    'license': 'AGPL-3',
    'depends': [
        'cosanum_base_data',
    ],
    'website': 'https://www.camptocamp.com',
    'data': [
        'data/res_groups.xml',
    ],
    'installable': True,
}
