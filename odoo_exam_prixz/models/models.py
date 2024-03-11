# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests

class odoo_exam_prixz(models.Model):
     
    _inherit= 'sale.order'
   
     
    rfc = fields.Char(
         string='rfc'
     )

    @api.onchange('partner_id')
    def _onchange_rfc(self):
        for rec in self:
            if not rec.partner_id.vat :
                rec.rfc = 'XAXX010101000'
                print('No se tiene el rfc del cliente')    
            rec.rfc = rec.partner_id.vat
            print('se tiene el rfc del cliente')    

      
    def consumo_api(self):
        r = requests.post('https://fakestoreapi.com/products')
        
        print(r.response)