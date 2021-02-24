# -*- coding: utf-8 -*-
{
    'name': "Modulo Comercio Electronico por Fede Lleó",

    'summary': """
       Este módulo es para añadir campos y botones a los productos 
       """,

    'description': """
       Añade el campo Referencia Interna y Código de Barras
    """,

    'author': "Bakata Solutions SL",
    'website': "https://www.bakata.es",
    'category': 'Sitio web',
    'version': '0.1.1',
    # Dependencias de módulos de Odoo
    'depends': ['website_sale', 'base'],

    # always loaded
    'data': [
         'views/main_view.xml', 
         
    ],
    ## only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}