# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Seller(models.Model):
    _inherit = "res.partner"

    segment_id = fields.Many2one(comodel_name="segment", string="Segmento", required=False, )