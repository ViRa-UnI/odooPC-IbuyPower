from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    custom_pc_id = fields.Many2one('pc.builder', string='Custom PC')

    @api.model
    def create(self, vals):
        if 'custom_pc_id' in vals:
            custom_pc = self.env['pc.builder'].browse(vals['custom_pc_id'])
            vals['name'] = custom_pc.name
        return super(StockMove, self).create(vals)

    def _action_done(self):
        res = super(StockMove, self)._action_done()
        for move in self:
            if move.custom_pc_id:
                move.custom_pc_id.write({'state': 'done'})
        return res

    def _action_cancel(self):
        res = super(StockMove, self)._action_cancel()
        for move in self:
            if move.custom_pc_id:
                move.custom_pc_id.write({'state': 'cancel'})
        return res