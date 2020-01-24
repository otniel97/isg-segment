# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Segment(models.Model):
    _name = "segment"

    name = fields.Char(string="Nombre", required=True, )
    image = fields.Binary(string="Imagen",  )