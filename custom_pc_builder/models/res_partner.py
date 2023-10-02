from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pc_builder_ids = fields.One2many(
        comodel_name='pc.builder',
        inverse_name='partner_id',
        string='PC Builder Orders',
    )

    @api.model
    def create(self, vals):
        record = super(ResPartner, self).create(vals)
        return record

    def write(self, vals):
        result = super(ResPartner, self).write(vals)
        return result

    def unlink(self):
        result = super(ResPartner, self).unlink()
        return result

    def copy(self, default=None):
        default = dict(default or {})
        return super(ResPartner, self).copy(default)