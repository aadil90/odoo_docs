# -*- coding: utf-8 -*-
{
    'name': "real_estate",

    'summary': """
        Real Estate documentaion..........     
    """,

    'description': """
        Real Estate Basic Odoo Module
    """,

    'author': "Muhammad Aadil Company",
    'website': "http://www.muhammadaadilcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/14.0/flectra/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 15,
}

