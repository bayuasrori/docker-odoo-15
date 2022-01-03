# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/addons/wisuda(http.Controller):
#     @http.route('//opt/addons/wisuda//opt/addons/wisuda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/addons/wisuda//opt/addons/wisuda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/addons/wisuda.listing', {
#             'root': '//opt/addons/wisuda//opt/addons/wisuda',
#             'objects': http.request.env['/opt/addons/wisuda./opt/addons/wisuda'].search([]),
#         })

#     @http.route('//opt/addons/wisuda//opt/addons/wisuda/objects/<model("/opt/addons/wisuda./opt/addons/wisuda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/addons/wisuda.object', {
#             'object': obj
#         })
