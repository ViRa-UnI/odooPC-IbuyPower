from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    custom_pc_order_id = fields.Many2one('pc.builder', string='Custom PC Order')

    @api.model
    def create(self, vals):
        if 'origin' in vals and 'SO' in vals['origin']:
            sale_order = self.env['sale.order'].search([('name', '=', vals['origin'])])
            if sale_order and sale_order.custom_pc_order_id:
                vals['custom_pc_order_id'] = sale_order.custom_pc_order_id.id
        return super(StockPicking, self).create(vals)

    def action_done(self):
        res = super(StockPicking, self).action_done()
        for picking in self:
            if picking.custom_pc_order_id and picking.picking_type_id.code == 'outgoing':
                picking.custom_pc_order_id.write({'state': 'done'})
        return res