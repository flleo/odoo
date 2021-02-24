#-*- coding: utf-8 -*-
# Codificación de caracteres

# Librerías necesarias de Odoo
from odoo import models, fields, api, _

# Librerías necesarias de Python
import logging

# Variable global para debuggear, imprime en /var/log/odoo/odoo-server.log
_logger = logging.getLogger(__name__)

# Clase para gestión modelo de datos

class modelo_empleados(models.Model):
    _inherit = 'hr.employee' # crea una clase a partir de la tabla hr.employee

    x_ss = fields.Char(string="Seguridad Social")
    x_internal_notes = fields.Text(string="Notas Internas")

    
    