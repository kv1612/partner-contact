# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, exceptions, fields, models, tools


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    block_delivery_route_update = fields.Boolean(
        string="Block Incoming Shipments Configuration"
    )
    block_reception_route_update = fields.Boolean(
        string="Block Outgoing Shipments Configuration"
    )
    block_manufacture_route_update = fields.Boolean(
        string="Block Manufacture Configuration"
    )

    def write(self, values):
        if tools.config["init"] or tools.config["update"]:
            # ignore the constraints when installing/updating modules,
            # which can make it fail
            return super().write(values)
        for wh in self:
            if (
                values.get('block_delivery_route_update')
                or wh.block_delivery_route_update
            ) and 'delivery_steps' in values:
                raise exceptions.UserError(_('Delivery Steps are blocked.'))

            if (
                values.get('block_reception_route_update')
                or wh.block_reception_route_update
            ) and 'reception_steps' in values:
                raise exceptions.UserError(_('Reception Steps are blocked.'))
            if (
                values.get('block_manufacture_route_update')
                or wh.block_manufacture_route_update
            ) and 'manufacture_steps' in values:
                raise exceptions.UserError(_('Manufacture Steps are blocked.'))
        return super().write(values)

    def _get_routes_values(self):
        values = super()._get_routes_values()
        if self.block_delivery_route_update:
            values.pop('delivery_route_id', None)
        if self.block_reception_route_update:
            values.pop('reception_route_id', None)
        if self.block_manufacture_route_update:
            values.pop('pbm_route_id', None)
        return values
