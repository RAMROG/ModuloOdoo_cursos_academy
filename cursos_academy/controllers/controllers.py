# -*- coding: utf-8 -*-
# from odoo import http


# class CursosAcademy(http.Controller):
#     @http.route('/cursos_academy/cursos_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cursos_academy/cursos_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cursos_academy.listing', {
#             'root': '/cursos_academy/cursos_academy',
#             'objects': http.request.env['cursos_academy.cursos_academy'].search([]),
#         })

#     @http.route('/cursos_academy/cursos_academy/objects/<model("cursos_academy.cursos_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cursos_academy.object', {
#             'object': obj

#         })
