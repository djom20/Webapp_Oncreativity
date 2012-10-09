#encoding:utf-8

from django.contrib import admin
from Gestor.models import cotizacion
from Gestor.models import empresa
from Gestor.models import factura
from Gestor.models import persona
from Gestor.models import servicio

admin.site.register(cotizacion)
admin.site.register(empresa)
admin.site.register(factura)
admin.site.register(persona)
admin.site.register(servicio)
