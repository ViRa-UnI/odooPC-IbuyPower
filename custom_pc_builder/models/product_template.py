from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_pc_component = fields.Boolean(string='Is PC Component', default=False)
    pc_component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard'),
        ('psu', 'Power Supply'),
        ('case', 'Case'),
    ], string='PC Component Type')

    @api.onchange('is_pc_component')
    def _onchange_is_pc_component(self):
        if not self.is_pc_component:
            self.pc_component_type = False

    @api.constrains('is_pc_component', 'pc_component_type')
    def _check_pc_component(self):
        for record in self:
            if record.is_pc_component and not record.pc_component_type:
                raise ValidationError("PC Component Type is required for PC Components.")