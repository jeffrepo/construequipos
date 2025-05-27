# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    fecha_entrega = fields.Date('Fecha de entrega')
    dias = fields.Float('Días')
    precio_dia = fields.Float('Precio por día')

    @api.onchange('dias','precio_dia')
    def _precio_dia(self):
        precio_unitario = self.dias * self.precio_dia
        self.price_unit = precio_unitario