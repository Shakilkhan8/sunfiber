# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class product_templete_fields(models.Model):
#     _name = 'product_templete_fields.product_templete_fields'
#     _description = 'product_templete_fields.product_templete_fields'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
