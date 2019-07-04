from odoo import models,fields,api
from odoo.exceptions import ValidationError

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
    
    @api.constrains('client_name')
    def _check_name(self):
        for val in self:
            if val['client_name']:
                if len(val["client_name"])<6:
                    raise ValidationError("name is too short, must be more than 6 character")
    
    _sql_constraints =[('client_name_unique','unique(client_name)','name already exists')]