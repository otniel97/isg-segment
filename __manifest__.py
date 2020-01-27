# -*- coding: utf-8 -*-
{
    'name': "isg_segment",

    'summary': """isg_segment Agrega segmento al vendedor""",

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
    'depends': ['base', 'odoo_marketplace', 'isg_frontend'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/segment_view.xml',
        'views/seller_view.xml',
        'views/seller_view_frontend.xml',
    ],
    'installable': True,
    "application":  True,
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}