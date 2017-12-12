from django.conf.urls import url
from apps.hotelapp.views import Index, UsuarioCreate, UsuarioList, UsuarioDelete
from apps.hotelapp.views import UsuarioUpdate, UsuarioShow, search, SucursalCreate
from apps.hotelapp.views import SucursalList, SucursalDelete, SucursalUpdate, SucursalShow
from apps.hotelapp.views import search_sucursal

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^nuevo/', UsuarioCreate.as_view(), name='usuario_crear'),
    url(r'^listar', UsuarioList.as_view(), name='usuario_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', UsuarioShow.as_view(), name='usuario_mostrar'),
    url(r'^buscar/$', search, name='usuario_buscar'),
    url(r'^nuevasuc/', SucursalCreate.as_view(), name='sucursal_crear'),
    url(r'^listasuc', SucursalList.as_view(), name='sucursal_listar'),
    url(r'^eliminasuc/(?P<pk>\d+)/$', SucursalDelete.as_view(), name='sucursal_eliminar'),
    url(r'^editasuc/(?P<pk>\d+)/$', SucursalUpdate.as_view(), name='sucursal_editar'),
    url(r'^muestrasuc/(?P<pk>\d+)/$', SucursalShow.as_view(), name='sucursal_mostrar'),
    url(r'^buscar_sucursal/$', search_sucursal, name='sucursal_buscar'),
]
