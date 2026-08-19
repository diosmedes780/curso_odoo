from odoo import models, fields

class SchoolSubjects(models.Model):
    _name = 'school.subjects'
    _description = 'School Subjects'

    name = fields.Char(string='Subject Name', required=True)
    teacher_id = fields.Many2one('res.partner', string='Teacher', required=True, domain=[('is_teacher', '=', True)])