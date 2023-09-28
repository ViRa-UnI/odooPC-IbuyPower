```python
from odoo import http
from odoo.http import request

class MainController(http.Controller):

    @http.route('/pc_builder', type='http', auth='user', website=True)
    def pc_builder(self, **kwargs):
        categories = request.env['product.category'].search([])
        return request.render('custom_pc_builder.pc_builder_template', {
            'categories': categories
        })

    @http.route('/pc_builder/add_to_cart', type='json', auth='user', methods=['POST'], website=True)
    def add_to_cart(self, product_id, quantity):
        order = request.website.sale_get_order(force_create=1)
        product = request.env['product.product'].browse(int(product_id))
        order._cart_update(product_id=int(product.id), add_qty=int(quantity))
        return {'cart_quantity': order.cart_quantity}

    @http.route('/pc_builder/remove_from_cart', type='json', auth='user', methods=['POST'], website=True)
    def remove_from_cart(self, line_id):
        order = request.website.sale_get_order(force_create=1)
        order._cart_update(line_id=int(line_id), set_qty=0)
        return {'cart_quantity': order.cart_quantity}
```