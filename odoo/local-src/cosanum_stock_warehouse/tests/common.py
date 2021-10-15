# Copyright 2020 Camptocamp (https://www.camptocamp.com)


from odoo.tests import common


class CosanumLogisticsCase(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.sch_wh = cls.env.ref("stock.warehouse0")
        cls.wer_wh = cls.env.ref("cosanum_stock_warehouse.warehouse_wer")
        cls.customer_location = cls.env.ref("stock.stock_location_customers")
        cls._create_base_data()

    @classmethod
    def _create_base_data(cls):
        cls.product = cls.env["product.product"].create(
            {"name": "Test Product", "barcode": "test", "type": "product"}
        )
        cls.product2 = cls.env["product.product"].create(
            {"name": "Test Product 2", "barcode": "test2", "type": "product"}
        )

    @classmethod
    def _update_qty_in_location(
        cls, location, product, quantity, package=None, lot=None, in_date=None
    ):
        quants = cls.env["stock.quant"]._gather(
            product, location, lot_id=lot, package_id=package, strict=True
        )
        # this method adds the quantity to the current quantity, so remove it
        quantity -= sum(quants.mapped("quantity"))
        cls.env["stock.quant"]._update_available_quantity(
            product,
            location,
            quantity,
            package_id=package,
            lot_id=lot,
            in_date=in_date,
        )
