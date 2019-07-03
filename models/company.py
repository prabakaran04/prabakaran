# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CompanyDetails(models.Model):
    _name = 'company.details'
    _rec_name ='name'
 
    name = fields.Char(string='company name', required =True)
    location = fields.Char(string='company location')
    contact_person = fields.Char(string = 'Contact Person')
    mobile = fields.Char()

   