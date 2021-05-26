# Copyright 2021 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # In standard odoo, the employee appraisal manager is a many2many_tags
    # widget trying to load the color of the employee. However, that color
    # field is restricted to "HR Officer" and cannot be read causing a ACL
    # error preventing to open the "My Profile" view.
    color = fields.Integer(groups="")
