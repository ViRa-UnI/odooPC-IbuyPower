from odoo import models, fields, api

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    custom_pc_builder_id = fields.Many2one('custom.pc.builder', string='Custom PC Builder')

    @api.model
    def create(self, vals):
        res = super(StockWarehouse, self).create(vals)
        if 'custom_pc_builder_id' in vals:
            res.custom_pc_builder_id = vals['custom_pc_builder_id']
        return res

    def write(self, vals):
        res = super(StockWarehouse, self).write(vals)
        if 'custom_pc_builder_id' in vals:
            self.custom_pc_builder_id = vals['custom_pc_builder_id']
        return res

    def unlink(self):
        for record in self:
            if record.custom_pc_builder_id:
                raise models.ValidationError('Cannot delete a warehouse that is linked to a custom PC builder.')
        return super(StockWarehouse, self).unlink()