from odoo import models, fields, api

class QualificationStudents(models.Model):
    _name = 'qualification.students'
    _description = 'Qualification Students'

    students_id = fields.Many2one('students.info', string='Student')
    school_subject_id = fields.Many2one('school.subjects', string='Subject')
    qualification = fields.Float(string='Qualification')
    state_subject = fields.Selection(
        string='State Subject',
        selection=[('approved', 'Approved'),
                   ('failed', 'Failed')],
        compute = '_check_qualification',
        store = True
    )

    @api.depends('qualification')
    def _check_qualification(self):
        for student in self:
            if student.qualification <= 69:
                student.state_subject = "failed"
            else:
                student.state_subject = "approved"