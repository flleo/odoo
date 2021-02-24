#-*- coding: utf-8 -*-
# Codificación de caracteres

# Librerías necesarias de Odoo
from odoo import http
from odoo.addons.website.controllers.main import Website
# Librerías necesarias de Python
import logging

# Variable global para debuggear, imprime en /var/log/odoo/odoo-server.log
_logger = logging.getLogger(__name__)

# Clase para gestión modelo de datos

class WebsiteInfo(Website):
    @http.route()
    def website_info(self):
        result = super(WebsiteInfo, self).website_info()
        result.qcontext['apps'] = result.qcontext['apps'].filtered(
            lambda x: x.name != 'website'
        )
        return result

    

    
