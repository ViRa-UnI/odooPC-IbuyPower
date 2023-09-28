from odoo import models, fields, api

class StockLocation(models.Model):
    _inherit = 'stock.location'

    custom_pc_builder_id = fields.Many2one('custom.pc.builder', string='PC Builder')

    @api.model
    def create(self, vals):
        if 'custom_pc_builder_id' in vals:
            pc_builder = self.env['custom.pc.builder'].browse(vals['custom_pc_builder_id'])
            pc_builder.write({'stock_location_id': vals['id']})
        return super(StockLocation, self).create(vals)

    def write(self, vals):
        if 'custom_pc_builder_id' in vals:
            pc_builder = self.env['custom.pc.builder'].browse(vals['custom_pc_builder_id'])
            pc_builder.write({'stock_location_id': vals['id']})
        return super(StockLocation, self).write(vals)

    def unlink(self):
        for record in self:
            if record.custom_pc_builder_id:
                raise models.ValidationError('Cannot delete a stock location that is referenced by a PC Builder.')
        return super(StockLocation, self).unlink()