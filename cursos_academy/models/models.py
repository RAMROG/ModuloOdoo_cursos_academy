# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cursos_academy(models.Model):
#     _name = 'cursos_academy.cursos_academy'
#     _description = 'cursos_academy.cursos_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class curso(models.Model):
    _name='cursos_academy.curso'
    _description='Permite definir las caracteristicas de los cursos'

    name = fields.Char(string='Nombre Curso', required=True)
    categoria = fields.Text(string='Categoria', required=True)
    description = fields.Text(string='Descripcion')
    duration   = fields.Integer(string='Duracion(horas)')
    price = fields.Float(string='Precio',requiered=True)

    #relaciones entre tablas
    maestro_ids = fields.One2many('cursos_academy.maestro', 'curso_id',string='maestro')

class maestro(models.Model):
    _name='cursos_academy.maestro'
    _description='Permite definir las caracteristicas del objeto Maestros'
    _order='identidad'

    name = fields.Char(string='Nombre Maestro', required=True)
    last_name = fields.Char(string='Apellido')
    identidad  = fields.Char(string='Identidad',required=True)
    edad = fields.Integer(string='Edad')
    description = fields.Text(string='Descripcion')
    curso_id = fields.Many2one('cursos_academy.curso',string='cursos')
