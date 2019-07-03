from odoo import models,fields,api

class ClientDetails(models.Model):
    _name = 'client.details'
    _rec_name='client_name'
    
    client_id = fields.Char(default ='new')
    client_name = fields.Char(string ='Client name')
    address = fields.Char(string ='Address')
    client_email = fields.Char(string = 'Email')
    mobile = fields.Char(string = 'Mobile')
    status = fields.Selection(string = 'status' , selection=[('gold', 'Gold'),('silver','Silver'),('bronze','bronze')])
    
    @api.model
    def create(self , vals):
        if vals.get('client_id','new') =='new':
            vals['client_id'] = self.env['ir.sequence']. next_by_code('client.details') or '/'
        return super(ClientDetails , self). create(vals)
    