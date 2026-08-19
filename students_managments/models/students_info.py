from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class Students(models.Model):
    _name = 'students.info'
    _rec_name = 'student_id'
    _description = 'Students'

    # name = fields.Char(string='Name', required=True)
    # last_name = fields.Char(string='Last Name')
    # age = fields.Integer(string='Age')
    # email = fields.Char(string='Email')
    student_id = fields.Many2one('res.partner', string='Students', required=True, domain=[('is_teacher', '=', False)])
    country_id = fields.Many2one('res.country', string='Country', related='student_id.country_id', store=True)   
    course_id = fields.Many2one('courses.students', string='Course')
    qualification_id = fields.One2many('qualification.students', 'students_id', string='Qualifications')
    grade_status = fields.Selection([
        ('approved', 'Approved'),
        ('fail', 'Fail')
    ], string='Grade Status')
    failed = fields.Boolean(string='Failed?', default=True)
    tags_ids = fields.Many2many('res.partner.category', string='Tags')
    address = fields.Char(string='Address link Google Maps')
    note = fields.Char(string='Note')
    age = fields.Integer(string='Age')

    def unlink(self):

        for record in self:
            if record.course_id:
                raise ValidationError("This student has a course that cannot be deleted.")

        return super().unlink()

    def copy(self, default=None):

        raise ValidationError("You cannot duplicate these records.")

    def reprobate(self):
        _logger.info("Reprobate student records")

        return {
            'name': 'Reprobate',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'wizard.qualification',
            'target': 'new',
            'context': {
                'default_student_id': self.id,
            }
        }

    @api.constrains('student_id')
    def _check_student_id(self):

        for record in self:

            if record.student_id and self.search_count(
                    [('student_id', '=', record.student_id),
                     ('id','!=', record.id )]):
                raise ValidationError("Student already exists")

    @api.onchange('age')
    def _onchange_age(self):

        for record in self:

            if record.age:
                if record.age <= 14:
                    raise ValidationError("The student must be over 14 years old.")