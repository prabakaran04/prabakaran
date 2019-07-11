from odoo import fields ,models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _name = 'sales.order'
    _rec_name='saleorder_id'
    
    @api.depends('order_line.product_name')
    def _all_amount(self):
        for order in self:
            for line in order.order_line:
                order.total_amount += line.sub_total
                order.untax_amount += line.untax_amount
                order.taxes += line.taxes
                
   
    saleorder_id = fields.Char(string='sale order', required =True)
    client_name = fields.Many2one('client.details',string='Client name', delegate = True)
    status = fields.Selection(related = 'client_name.status', string ="status")
   
#     product_order_line = fields.One2many('sale.order.lines','sale_order_line' 
    validity_date = fields.Date()
    payment_terms = fields.Selection(string="Payment Terms" , selection=[('Immediate payment','immediate payment'),("15 days" , "15 days"),
                                                                  ('30 net days','30 net days')])
    order_line = fields.One2many('sale.order.lines', 'sale_order_line')
    total_amount = fields.Float(string ='Total', compute ='_all_amount')
    untax_amount = fields.Float(compute ='_all_amount')
    taxes = fields.Float(compute ='_all_amount')
    state = fields.Selection(selection=[('quotation_create','Quotation'),('quotation_send', 'Quotation send'),('confirm_sale_order','sales order')],
                             default = 'quotation_create')
    
    
    @api.multi
    def send_quotation(self):
        self.ensure_one()
        self.write({'state':'quotation_send'})
        
    @api.multi
    def confirm_sale_order(self):
        self.ensure_one()
        self.write({'state':'confirm_sale_order'})
        
   
    @api.onchange('total_amount')
    def _calc_amount(self):
         self.ensure_one()
         if self.total_amount > 12000:
            raise ValidationError("Limit amount exceeded, You can not confirm sale order for more than 12000")
    
    
#     @api.depends('product_name')
#     def _get_stock(self):
#          a =["paraceatamol","web technology"]
#          for i in a:
#              if self.product_name.item_name == i:
#                  self.product_order_line = self.env['stock.details'].search([( 'item_name' ,'=', i)])
        
class SaleOrderLines(models.Model):
    _name ='sale.order.lines'
    _rec_name ='sale_order_line'    
    
    sale_order_line = fields.Many2one('sales.order',string ='sale order')
    product_name = fields.Many2one('stock.details')
    description = fields.Char()
    product_quantity = fields.Float(string='ordered Quantity', default ='1')
    units_price = fields.Float()
    tax = fields.Selection(string = 'taxes', selection=[('5','5'),('10','10'),('15','15'),('20','20')])
    sub_total = fields.Float()
    in_stock = fields.Integer(related = "product_name.quantity", string= "In stock")
    untax_amount = fields.Float()
    taxes = fields.Float()
    
    
   
        
    @api.onchange('tax','product_quantity','units_price')
    def caltax(self):
        a = ['5','10','15','20']
        for x in a:
            if x == self.tax:
                c= int(x)
                self.sub_total = (self.units_price* self.product_quantity)+((self.units_price* self.product_quantity)* c/100)
                self.untax_amount = (self.units_price* self.product_quantity)
                self.taxes = ((self.units_price* self.product_quantity)* c/100)
                  
                  