# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ventassuma(models.Model):
    _inherit = 'stock.picking'
    
    registros_inc = fields.Float('Registros totales')

    @api.model
    def sumar_demandas(self):
        pickings = self.search([])
        for picking in pickings:
            total_quantity = 0
            for move in picking.move_lines:
                if move.picking_type_id.code == 'incoming':
                    total_quantity += move.product_uom_qty
            picking.registros_inc = total_quantity

