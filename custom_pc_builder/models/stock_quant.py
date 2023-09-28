from odoo import api, fields, models

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    custom_pc_component_id = fields.Many2one('product.product', string='Custom PC Component')

    @api.model
    def create(self, vals):
        if 'custom_pc_component_id' in vals:
            product = self.env['product.product'].browse(vals['custom_pc_component_id'])
            if product.is_custom_pc_component:
                vals['product_id'] = product.id
        return super(StockQuant, self).create(vals)

    def write(self, vals):
        if 'custom_pc_component_id' in vals:
            product = self.env['product.product'].browse(vals['custom_pc_component_id'])
            if product.is_custom_pc_component:
                vals['product_id'] = product.id
        return super(StockQuant, self).write(vals)