from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    pc_component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
        ('power_supply', 'Power Supply'),
        ('case', 'Case'),
    ], string='PC Component Type')

    @api.onchange('pc_component_type')
    def _onchange_pc_component_type(self):
        if self.pc_component_type:
            self.categ_id = self.env.ref('custom_pc_builder.pc_component_category_' + self.pc_component_type).id

    @api.model
    def create(self, vals):
        if 'pc_component_type' in vals and 'categ_id' not in vals:
            vals['categ_id'] = self.env.ref('custom_pc_builder.pc_component_category_' + vals['pc_component_type']).id
        return super(ProductProduct, self).create(vals)

    def write(self, vals):
        if 'pc_component_type' in vals and 'categ_id' not in vals:
            vals['categ_id'] = self.env.ref('custom_pc_builder.pc_component_category_' + vals['pc_component_type']).id
        return super(ProductProduct, self).write(vals)