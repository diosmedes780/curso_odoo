from odoo import models, fields
from odoo.exceptions import ValidationError


class QualificationWizard(models.TransientModel):
    _name = "wizard.qualification"

    student_id = fields.Many2one('students.info', string='Students')
    note = fields.Char(string='Note')

    def reprobate(self):

        if not self.student_id:
            raise ValidationError('No have student')

        student = self.env['students.info'].browse(self.student_id.id)

        if student:
            student.failed = True
            student.note = self.note
