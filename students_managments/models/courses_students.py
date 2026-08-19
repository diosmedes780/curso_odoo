from odoo import models, fields

class Courses(models.Model):
    _name = 'courses.students'
    _description = 'Courses'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True)