"""
Definition of forms.
"""

from django import forms
from django.forms.models import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *
from django.views.generic.detail import DetailView
from django.views.generic import ListView

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =('nombre','paterno','materno','edad','email','direccion','tcredito')
        labels = {
            'nombre': 'Nombre',
            'paterno': 'Apellido paterno',
            'materno': 'Apellido materno',
            'edad': 'Edad',
            'direccion': 'Dirección',
            'tcredito' : 'Número de tarjeta de crédito'
            }
       
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('cantidadNoches',)
        labels = {
            'cantidadNoches' : 'Cantidad de noches'
            }
