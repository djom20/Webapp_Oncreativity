#encoding:utf-8
from django.contrib.auth.models import User
from django.db import models

class persona(models.Model):
    usuario = models.ForeignKey(User)
    cedula = models.CharField(max_length=15, unique=True, primary_key=True)
    cargo = models.CharField(max_length=70)
    celular = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50, unique=True)
    barrio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


def __unicode__(self):
    return self.usuario



class factura(models.Model):
    ident= models.IntegerField(max_length=15, unique=True, primary_key=True)
    fechacorte = models.DateField(max_length=70)
    total = models.CharField(max_length=100)


def __unicode__(self):
    return self.ident


class empresa(models.Model):
    usuario = models.ForeignKey(User)
    nit = models.IntegerField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=70, unique=True)
    direccion = models.CharField(max_length=50, unique=True)
    website = models.URLField(verify_exists=True, max_length=200)
    estado = models.BooleanField(default='True')


def __unicode__(self):
    return self.nombre


class servicio(models.Model):
    ident = models.IntegerField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=70, unique=True)
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField(max_length=10)
    estado = models.BooleanField(default='True')


def __unicode__(self):
    return self.nombre


class cotizacion(models.Model):
    ident = models.IntegerField(max_length=10, unique=True, primary_key=True)
    descripcion = models.CharField(max_length=50)


def __unicode__(self):
    return self.ident
