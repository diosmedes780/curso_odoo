from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'


    is_teacher = fields.Boolean(string='Is Teacher?', default=False)