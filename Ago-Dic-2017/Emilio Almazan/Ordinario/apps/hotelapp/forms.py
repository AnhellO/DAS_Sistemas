from django import forms
from apps.hotelapp.models import Usuario, Sucursal

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = [
			'nombres',
			'apellidos',
			'fecha_nacimiento',
			'email',
			'hotel_hospedaje',
			'habitacion'
		]

		labels = {
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'fecha_nacimiento': 'Fecha de Nacimiento',
			'email': 'Correo Electronico',
			'hotel_hospedaje': 'Hotel',
			'habitacion': 'Habitacion'
		}

		widgets = {
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'hotel_hospedaje': forms.Select(attrs={'class':'form-control'}),
			'habitacion': forms.TextInput(attrs={'class':'form-control'}),
		}


class SucursalForm(forms.ModelForm):
	class Meta:
		model = Sucursal
		fields = [
			'nombre'
		]

		labels = {
			'nombre': 'Nombre'
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'})
		}
