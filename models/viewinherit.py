from odoo import fields,models,api

class InheritCompany(models.Model):
    _inherit = 'company.details'
    
    company_email = fields.Char()
    description = fields.Html()
    