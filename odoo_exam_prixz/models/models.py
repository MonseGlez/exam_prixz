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
        
        if self.partner_id.vat:
            self.rfc = self.partner_id.vat 
        else: 
            self.rfc= 'XAXX010101000'
       
      
    def consumo_api(self):
        r = requests.get('https://fakestoreapi.com/products')        
        print(r.text)