from odoo import models, fields, api

class PcBuilder(models.Model):
    _name = 'pc.builder'
    _description = 'PC Builder'

    name = fields.Char(string='Name', required=True)
    cpu = fields.Many2one('product.product', string='CPU', domain=[('is_cpu', '=', True)])
    gpu = fields.Many2one('product.product', string='GPU', domain=[('is_gpu', '=', True)])
    ram = fields.Many2one('product.product', string='RAM', domain=[('is_ram', '=', True)])
    storage = fields.Many2one('product.product', string='Storage', domain=[('is_storage', '=', True)])
    case = fields.Many2one('product.product', string='Case', domain=[('is_case', '=', True)])
    power_supply = fields.Many2one('product.product', string='Power Supply', domain=[('is_power_supply', '=', True)])
    motherboard = fields.Many2one('product.product', string='Motherboard', domain=[('is_motherboard', '=', True)])
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')

    @api.depends('cpu', 'gpu', 'ram', 'storage', 'case', 'power_supply', 'motherboard')
    def _compute_total_price(self):
        for record in self:
            total_price = 0
            if record.cpu:
                total_price += record.cpu.lst_price
            if record.gpu:
                total_price += record.gpu.lst_price
            if record.ram:
                total_price += record.ram.lst_price
            if record.storage:
                total_price += record.storage.lst_price
            if record.case:
                total_price += record.case.lst_price
            if record.power_supply:
                total_price += record.power_supply.lst_price
            if record.motherboard:
                total_price += record.motherboard.lst_price
            record.total_price = total_price

    def action_create_sale_order(self):
        sale_order = self.env['sale.order'].create({
            'partner_id': self.env.user.partner_id.id,
            'pc_builder_id': self.id,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.cpu.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.gpu.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.ram.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.storage.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.case.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.power_supply.id,
            'product_uom_qty': 1,
        })
        self.env['sale.order.line'].create({
            'order_id': sale_order.id,
            'product_id': self.motherboard.id,
            'product_uom_qty': 1,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'view_mode': 'form',
        }