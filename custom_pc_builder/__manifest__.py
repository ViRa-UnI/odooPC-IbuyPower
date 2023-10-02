{
    'name': 'Custom PC Builder',
    'version': '16.0.1.0.0',
    'category': 'Website',
    'summary': 'Custom PC Building Module for E-commerce',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale', 'stock', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/pc_builder_view.xml',
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/sale_order_view.xml',
        'views/sale_order_line_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_move_view.xml',
        'views/stock_quant_view.xml',
        'views/stock_inventory_view.xml',
        'views/stock_warehouse_view.xml',
        'views/stock_location_view.xml',
        'views/res_partner_view.xml',
        'views/templates.xml',
        'data/pc_builder_demo.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
    This module allows customers to build their own custom PC on your e-commerce website.
    Features include:
    - Selection of components
    - Real-time price calculation
    - Stock management
    - Order management
    """
}