# -*- coding: utf-8 -*-
{
    'name': "Modulo Empleados por Fede Lleó",

    'summary': """
       Este módulo es para añadir campos personalizados al módulo de Empleados 
       """,

    'description': """
         Añade el campo S.S. y la pestaña Notas Internas
    """,

    'author': "Bakata Solutions SL",
    'website': "https://www.bakata.es",
    'category': 'Empleados',
    'version': '0.1.1',
    # Dependencias de módulos de Odoo
    'depends': ['hr', 'base'],

    # always loaded
    'data': [
         'views/vista_empleados.xml',        
    ],
    ## only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}