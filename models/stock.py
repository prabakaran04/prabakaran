from odoo import api,fields,models

class StockDetails(models.Model):
    _name = 'stock.details'
    _rec_name='item_name'
    
    item_name = fields.Char(string = "Item name" , required =True)
    item_details = fields.Char(string = "Item Details")
    item_price = fields.Integer(string ="Item price")
    quantity = fields.Integer(string = 'Quantity')
    company_name = fields.Many2one('company.details',string ="Company name", required = True , delegate = True , domain =[('name','=','cilpa')])
    warehouse_name = fields.Char()
    expire_date = fields.Date(string = "Expire Date")
   
    item_quantity = fields.Float(string ="quantity",  default = 1 )
    
    _sql_constraints=[('item_name_item_details_check','CHECK(item_name != item_details)', 'the item name should not be same as item details')]
   
    
    