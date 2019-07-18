# -*- coding: utf-8 -*-
{
    'name': "medicalmanagement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/reportpaper_format.xml',
        'security/ir.model.access.csv',
        'wizards/client_wizard_view.xml',
        'views/views.xml',
        'views/stock_view.xml',
        'views/clients_view.xml',
        'views/sale_view.xml',
        'views/viewinherit_view.xml',
        'views/layout.xml',
        'views/report_action.xml',
        'views/report_sale_template.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}