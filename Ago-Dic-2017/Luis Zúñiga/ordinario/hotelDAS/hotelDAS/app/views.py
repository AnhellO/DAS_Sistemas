# -*- coding: utf-8 -*-
"""
Definition of views.
"""
from django.http import HttpResponse, Http404 
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import *
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from app.models import *

import locale
import django.utils.encoding as _
#from django.utils.translation import ugettext_lazy as _

locale.setlocale( locale.LC_ALL, 'English_United States.1252' )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
           
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
       'app/about.html', 
        {
            'title':'Diseño y arquitectura de software.',
            
            'year':datetime.now().year,
        },'text/html'
    )
 
def registracliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            new_cliente= form.save(commit = False)
            request.session['tcredito'] = new_cliente.tcredito
            request.session['nombre'] = new_cliente.nombre
            request.session['paterno'] = new_cliente.paterno
            request.session['materno']  = new_cliente.materno
            request.session['edad'] = new_cliente.edad
            request.session['email'] = new_cliente.email
            request.session['direccion'] = new_cliente.direccion
            print(request.session['tcredito'])
            print(request.session['nombre'])
            print(request.session['paterno'])
            print(request.session['materno'])
            print(request.session['edad'])
            print(request.session['email'])
            print(request.session['direccion'])            
            return HttpResponseRedirect('reservacion/')
    else:
       form = ClienteForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registracliente.html',
        {
            'title':'Registro de cliente',
            'year':datetime.now().year,
            'form': form
        }
    )

def reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        print("formato válido: {}".format(form.is_valid()))
        if  form.is_valid():
            totalApagar = 0
            print(request.session['tcredito'])
            print(request.session['nombre'])
            print(request.session['paterno'])
            print(request.session['materno'])
            print(request.session['edad'])
            print(request.session['email'])
            print(request.session['direccion'])
            Nombre = request.session['nombre']
            Paterno = request.session['paterno']
            Materno = request.session['materno']
            Direccion = request.session['direccion']
            Edad = request.session['edad']
            Email = request.session['email']
            Tcredito = request.session['tcredito']
            cliente = Cliente(nombre = Nombre, paterno = Paterno, materno = Materno, direccion = Direccion, edad = Edad, email = Email, tcredito = Tcredito)
            cliente.save()
            new_reservacion = form.save(commit = False)
            totalApagar = new_reservacion.cantidadNoches*800
            Cantidad = new_reservacion.cantidadNoches
            request.session['cantidad'] = Cantidad
            request.session['total'] = totalApagar
            print('Variables de request session{}\n{}'.format(request.session['cantidad'],request.session['total']))
            print("total a pagar: {}\nCantidad de noches: {}\nTarjeta de crédito: {}".format(totalApagar,Cantidad,Tcredito))
            reservacion = Reservacion(totalAPagar = totalApagar,tcredito = cliente, cantidadNoches = Cantidad)
            reservacion.save()
            return HttpResponseRedirect('/muestrareservacion/')
    else:
        form = ReservaForm()
        return render(
            request, 'app/reservacion.html',
            {
                'title':'Registro de cliente',
                'year':datetime.now().year,
                'form' : form
            }
            
       )


def muestraReservacion(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/muestrareservacion.html',
        {
            'message':'Datos de su reservación',
            'year':datetime.now().year,
            'nombre' : request.session['nombre'],
            'paterno' : request.session['paterno'],
            'materno' : request.session['materno'],
            'direccion' : request.session['direccion'],
            'noches' : request.session['cantidad'],
            'total' : locale.currency( request.session['total'], grouping = True )
        }
    )
