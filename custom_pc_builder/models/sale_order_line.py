from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    custom_pc_id = fields.Many2one('pc.builder', string='Custom PC')

    @api.onchange('custom_pc_id')
    def _onchange_custom_pc_id(self):
        if self.custom_pc_id:
            self.product_id = self.custom_pc_id.product_id
            self.price_unit = self.custom_pc_id.price

    @api.multi
    def _prepare_invoice_line(self, qty):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        if self.custom_pc_id:
            res['custom_pc_id'] = self.custom_pc_id.id
        return res

    @api.multi
    def unlink(self):
        for line in self:
            if line.custom_pc_id:
                line.custom_pc_id.unlink()
        return super(SaleOrderLine, self).unlink()