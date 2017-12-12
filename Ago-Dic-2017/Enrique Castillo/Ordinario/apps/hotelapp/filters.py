import django_filters
from apps.hotelapp.models import Usuario, Sucursal

class UsuarioFilter(django_filters.FilterSet):
	class Meta:
		model = Usuario
		fields = ['nombres', 'apellidos', 'email',]

class SucursalFilter(django_filters.FilterSet):
	class Meta:
		model = Sucursal
		fields = ['nombre']
