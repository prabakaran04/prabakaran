# -*- coding: utf-8 -*-
from odoo import http

# class Medicalmanagement(http.Controller):
#     @http.route('/medicalmanagement/medicalmanagement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/medicalmanagement/medicalmanagement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('medicalmanagement.listing', {
#             'root': '/medicalmanagement/medicalmanagement',
#             'objects': http.request.env['medicalmanagement.medicalmanagement'].search([]),
#         })

#     @http.route('/medicalmanagement/medicalmanagement/objects/<model("medicalmanagement.medicalmanagement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('medicalmanagement.object', {
#             'object': obj
#         })