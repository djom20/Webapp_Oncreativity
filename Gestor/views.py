from Gestor.models import cotizacion
from Gestor.models import empresa
from Gestor.models import factura
from Gestor.models import persona
from Gestor.models import servicio

#from django.contrib.auth.models import User
#from django.core.mail import EmailMessage
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404
#from gestorPersonas.forms import ContactoForm
from django.shortcuts import render_to_response
from django.template import RequestContext

#Gestion de usuarios
#from django.contrib.auth import authenticate
#from django.contrib.auth import login
#from django.contrib.auth import logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm

def lista_cotizaciones(request):
    cotizaciones = cotizacion.objects.all()
    return render_to_response('lista_cotizaciones.html', {'lista': cotizaciones}, context_instance=RequestContext(request))


def lista_empresas(request):
    empresas = empresa.objects.all()
    return render_to_response('lista_empresas.html', {'lista': empresas}, context_instance=RequestContext(request))


def lista_facturas(request):
    facturas = factura.objects.all()
    return render_to_response('lista_facturas.html', {'lista': facturas}, context_instance=RequestContext(request))


def lista_personas(request):
    personas = persona.objects.all()
    return render_to_response('lista_personas.html', {'lista': personas}, context_instance=RequestContext(request))


def lista_servicios(request):
    servicios = servicio.objects.all()
    return render_to_response('lista_servicios.html', {'lista': servicios}, context_instance=RequestContext(request))
