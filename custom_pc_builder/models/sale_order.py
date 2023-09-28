from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pc_builder_id = fields.Many2one('pc.builder', string='PC Builder')

    @api.onchange('pc_builder_id')
    def _onchange_pc_builder_id(self):
        if self.pc_builder_id:
            self.order_line = [(5, 0, 0)]
            for line in self.pc_builder_id.pc_component_ids:
                product = line.product_id
                vals = {
                    'product_id': product.id,
                    'name': product.name,
                    'product_uom_qty': line.quantity,
                    'price_unit': product.lst_price,
                }
                self.order_line = [(0, 0, vals)]

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.pc_builder_id:
                order.pc_builder_id.write({'state': 'sold'})
        return res