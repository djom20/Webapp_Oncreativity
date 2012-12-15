from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cotizaciones', 'Gestor.views.lista_cotizaciones'),
    url(r'^personas', 'Gestor.views.lista_personas'),
    url(r'^servicios', 'Gestor.views.lista_servicios'),
    url(r'^empresas', 'Gestor.views.lista_empresas'),
    url(r'^facturas', 'Gestor.views.lista_facturas'),


    
    url(r'^$', 'oncreativity.views.home', name='home'),
    url(r'^contacto/$', 'oncreativity.views.contacto', name='contacto'),
    #url(r'^usuario/nuevo$', 'gestorPersonas.views.nuevo_usuario'),
    #url(r'^ingresar/$', 'gestorPersonas.views.ingresar'),
    #url(r'^privado/$', 'gestorPersonas.views.ingresar'),
)
