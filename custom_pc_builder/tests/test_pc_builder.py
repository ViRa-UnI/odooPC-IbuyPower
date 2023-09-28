from odoo.tests.common import TransactionCase

class TestPCBuilder(TransactionCase):

    def setUp(self):
        super(TestPCBuilder, self).setUp()
        self.PCBuilder = self.env['pc.builder']
        self.ProductTemplate = self.env['product.template']
        self.SaleOrder = self.env['sale.order']

    def test_create_pc_builder(self):
        pc_builder = self.PCBuilder.create({
            'name': 'Test PC Builder',
            'description': 'This is a test PC Builder',
        })
        self.assertEqual(pc_builder.name, 'Test PC Builder')

    def test_create_product_template(self):
        product_template = self.ProductTemplate.create({
            'name': 'Test Product Template',
            'description': 'This is a test Product Template',
        })
        self.assertEqual(product_template.name, 'Test Product Template')

    def test_create_sale_order(self):
        sale_order = self.SaleOrder.create({
            'name': 'Test Sale Order',
            'description': 'This is a test Sale Order',
        })
        self.assertEqual(sale_order.name, 'Test Sale Order')

    def test_pc_builder_flow(self):
        pc_builder = self.PCBuilder.create({
            'name': 'Test PC Builder',
            'description': 'This is a test PC Builder',
        })
        product_template = self.ProductTemplate.create({
            'name': 'Test Product Template',
            'description': 'This is a test Product Template',
        })
        sale_order = self.SaleOrder.create({
            'name': 'Test Sale Order',
            'description': 'This is a test Sale Order',
        })
        pc_builder.product_template_id = product_template.id
        sale_order.pc_builder_id = pc_builder.id
        self.assertEqual(pc_builder.product_template_id, product_template)
        self.assertEqual(sale_order.pc_builder_id, pc_builder)