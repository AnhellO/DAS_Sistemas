from django import forms
from apps.hotel.models import Cliente, Habitacion, Reservacion

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
            'Nombre',
            'ApellidoPaterno',
            'ApellidoMaterno',
            'FechaNacimiento',
            'Telefono',
            'Email',
        ]

        labels = {
            'Nombre': 'Nombre',
            'ApellidoPaterno': 'Apellido Paterno',
            'ApellidoMaterno': 'Apellido Materno',
            'FechaNacimiento': 'Fecha de Nacimiento',
            'Telefono': 'Telefono',
            'Email': 'Email',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'ApellidoPaterno': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'ApellidoMaterno': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'FechaNacimiento': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'Telefono': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'Email': forms.TextInput(attrs = {'class':'form-control input-sm'}),
        }


class HabitacionForm(forms.ModelForm):

    class Meta:
        model = Habitacion

        fields = [
            'Nombre',
            'Precio',
            'Estado',
        ]

        labels = {
            'Nombre': 'Nombre',
            'Precio': 'Precio',
            'Estado': 'Estado',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs = {'class':'form-control input-sm'}),
            'Precio': forms.NumberInput(attrs = {'class':'form-control input-sm'}),
            'Estado': forms.CheckboxInput(attrs = {'class':'form-control input-sm'}),
        }

class ReservacionForm(forms.ModelForm):

    class Meta:
        model = Reservacion

        fields = [
            'cliente',
            'habitacion',
            'FechaReservacion',
            'formaPago',
            'numPersonas',
        ]

        labels = {
            'cliente': 'Cliente',
            'habitacion': 'Habitacion',
            'FechaReservacion': 'Fecha de reservacion',
            'formaPago': 'Forma de Pago',
            'numPersonas': 'Numero de Personas',
        }

        widgets = {
            'cliente': forms.Select(attrs = {'class':'form-control input-sm'}),
            'habitacion': forms.Select(attrs = {'class':'form-control input-sm'}),
            'FechaReservacion': forms.DateInput(attrs = {'class':'form-control input-sm'}),
            'formaPago': forms.Select(attrs = {'class':'form-control input-sm'}),
            'numPersonas': forms.Select(attrs = {'class':'form-control input-sm'}),
        }
