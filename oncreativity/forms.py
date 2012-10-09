#encoding:utf-8

from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)

