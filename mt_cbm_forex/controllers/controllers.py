# -*- coding: utf-8 -*-
from odoo import http

# class MtCbmForest(http.Controller):
#     @http.route('/mt_cbm_forest/mt_cbm_forest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mt_cbm_forest/mt_cbm_forest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mt_cbm_forest.listing', {
#             'root': '/mt_cbm_forest/mt_cbm_forest',
#             'objects': http.request.env['mt_cbm_forest.mt_cbm_forest'].search([]),
#         })

#     @http.route('/mt_cbm_forest/mt_cbm_forest/objects/<model("mt_cbm_forest.mt_cbm_forest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mt_cbm_forest.object', {
#             'object': obj
#         })