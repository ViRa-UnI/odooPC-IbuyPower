from odoo import models, fields, api

class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    custom_pc_builder_id = fields.Many2one('custom.pc.builder', string='Custom PC Builder')

    @api.model
    def create(self, vals):
        if 'custom_pc_builder_id' in vals:
            pc_builder = self.env['custom.pc.builder'].browse(vals['custom_pc_builder_id'])
            vals['location_id'] = pc_builder.location_id.id
        return super(StockInventory, self).create(vals)

    def action_validate(self):
        self.ensure_one()
        if self.custom_pc_builder_id:
            self.custom_pc_builder_id.state = 'done'
        return super(StockInventory, self).action_validate()

    def action_cancel_draft(self):
        self.ensure_one()
        if self.custom_pc_builder_id:
            self.custom_pc_builder_id.state = 'draft'
        return super(StockInventory, self).action_cancel_draft()