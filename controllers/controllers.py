# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/isgSegment(http.Controller):
#     @http.route('/extra-addons/isg_segment/extra-addons/isg_segment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/isg_segment/extra-addons/isg_segment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/isg_segment.listing', {
#             'root': '/extra-addons/isg_segment/extra-addons/isg_segment',
#             'objects': http.request.env['extra-addons/isg_segment.extra-addons/isg_segment'].search([]),
#         })

#     @http.route('/extra-addons/isg_segment/extra-addons/isg_segment/objects/<model("extra-addons/isg_segment.extra-addons/isg_segment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/isg_segment.object', {
#             'object': obj
#         })