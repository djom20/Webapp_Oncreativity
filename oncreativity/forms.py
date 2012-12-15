#encoding:utf-8

from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	nombre = forms.CharField()
	correo = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)

