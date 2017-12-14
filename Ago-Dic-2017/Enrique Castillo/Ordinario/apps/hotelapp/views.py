from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

from apps.hotelapp.models import Usuario
from apps.hotelapp.forms import UsuarioForm
from apps.hotelapp.filters import UsuarioFilter

from apps.hotelapp.models import Sucursal
from apps.hotelapp.forms import SucursalForm
from apps.hotelapp.filters import SucursalFilter

# Create your views here.

class Index(TemplateView):
    template_name = "home.html"

class UsuarioCreate(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'hotelapp/usuario_form.html'
	success_url = reverse_lazy('usuarios:usuario_listar')

class UsuarioList(ListView):
	queryset = Usuario.objects.order_by('id')
	template_name = 'hotelapp/usuarios_list.html'
	paginate_by = 5

class UsuarioUpdate(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'hotelapp/usuario_form.html'
	success_url = reverse_lazy('usuarios:usuario_listar')

class UsuarioDelete(DeleteView):
	model = Usuario
	template_name = 'hotelapp/usuario_delete.html'
	success_url = reverse_lazy('usuarios:usuario_listar')

class UsuarioShow(DetailView):
	model = Usuario
	template_name = 'hotelapp/usuario_show.html'


class SucursalCreate(CreateView):
	model = Sucursal
	form_class = SucursalForm
	template_name = 'hotelapp/sucursal_form.html'
	success_url = reverse_lazy('sucursales:sucursal_listar')

class SucursalList(ListView):
	queryset = Sucursal.objects.order_by('id')
	template_name = 'hotelapp/sucursal_list.html'
	paginate_by = 5

class SucursalUpdate(UpdateView):
	model = Sucursal
	form_class = SucursalForm
	template_name = 'hotelapp/sucursal_form.html'
	success_url = reverse_lazy('sucursales:sucursal_listar')

class SucursalDelete(DeleteView):
	model = Sucursal
	template_name = 'hotelapp/sucursal_delete.html'
	success_url = reverse_lazy('sucursales:sucursal_listar')

class SucursalShow(DetailView):
	model = Sucursal
	template_name = 'hotelapp/sucursal_show.html'

def search(request):
	usuario_list = Usuario.objects.all()
	usuario_filter = UsuarioFilter(request.GET, queryset=usuario_list)
	return render(request, 'hotelapp/usuario_list2.html', {'filter': usuario_filter})

def search_sucursal(request):
	sucursal_list = Sucursal.objects.all()
	sucursal_filter = SucursalFilter(request.GET, queryset=sucursal_list)
	return render(request, 'hotelapp/sucursal_list2.html', {'filter': sucursal_filter})
