#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext


from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from oncreativity.forms import ContactoForm

#from gestorPersonas.models import persona

#Gestion de usuarios
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login
#from django.contrib.auth import authenticate
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def contacto(request):
	if request.method == 'POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid:
			titulo = 'Mensaje desde la web de AltiviaOT'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'comunicarse a: ' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to = ['djom202@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm
	return render_to_response('contacto.html', {'formulario':formulario}, context_instance=RequestContext(request))

# def nuevo_usuario(request):
#     if request.method == 'POST':
#         formulario = UserCreationForm(request.POST)
#         if formulario.is_valid:
#             formulario.save()
#             return HttpResponseRedirect('/')
#         else:
#             formulario = UserCreationForm()
#         return render_to_response('nuevousuario.html', {'formulario': formulario}, context_instance=RequestContext(request))


# @login_required(login_url='/ingresar')
# def privado(request):
#     usuario = request.User
#     return render_to_response('privado.html', {'usuario': usuario}, context_instance=RequestContext(request))


# def ingresar(request):
#     if not request.user.is_anonymous():
#         return HttpResponseRedirect('/privado')
#     if request.method == 'POST':
#         formulario = AuthenticationForm(request.POST)
#         if formulario.is_valid:
#             usuario = request.POST['username']
#             clave = request.POST['password']
#             acceso = authenticate(username=usuario, password=clave)
#             if acceso is not None:
#                 if acceso.is_active:
#                     login(request. acceso)
#                     return HttpResponseRedirect('/privado')
#                 else:
#                     return render_to_response('nousuario.html', context_instance=RequestContext(request))
#             else:
#                 formulario = AuthenticationForm()
#             return render_to_response('ingresar.html', {'formulario': formulario}, context_instance=RequestContext(request))
