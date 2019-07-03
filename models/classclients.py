from odoo import models,fields,api

class ClassClients(models.Model):
    _inherit = 'client.details'
    
    
    customer_image = fields.Binary()