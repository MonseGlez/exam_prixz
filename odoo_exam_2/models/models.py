# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ventassuma(models.Model):
    _inherit = 'stock.picking'
    registros_inc = fields.Integer('registros totales' )

    def mostrar_incoming(self):
        registros_in  = self.env['stock.picking'].sudo().search([('name','ilike','IN')])

        for reg in registros_in.move_ids_without_package :
            x = x + reg.product_oum_qty

        self.registros_inc = x

    

