from odoo import fields,models,api

class ClientWizard(models.TransientModel):
    _name = 'client.wizard'
    
    name = fields.Char(required= True)