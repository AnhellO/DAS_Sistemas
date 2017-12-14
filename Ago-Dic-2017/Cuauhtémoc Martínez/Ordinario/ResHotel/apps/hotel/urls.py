from django.urls import path
from apps.hotel.views import *

urlpatterns = [
    path('Cliente/', index_Cliente, name = 'Cindex'),
    path('Cliente/nuevo', cliente_view, name = 'crear_cliente'),
    path('Cliente/ver', lista_cliente, name = 'ver_cliente'),
    path('Cliente/editar/<idCl>', editar_cliente, name = 'editar_cliente'),
    path('Cliente/eliminar/<idCl>', eliminar_cliente, name = 'eliminar_cliente'),
    path('Habitacion/', index_Habitacion, name = 'Hindex'),
    path('Habitacion/nuevo', habitacion_view, name = 'crear_habitacion'),
    path('Habitacion/ver', lista_habitacion, name = 'ver_habitacion'),
    path('Habitacion/editar/<idHab>', editar_habitacion, name = 'editar_habitacion'),
    path('Habitacion/eliminar/<idHab>', eliminar_habitacion, name = 'eliminar_habitacion'),
    path('Reservacion/', index_Reservacion, name = 'Rindex'),
    path('Reservacion/nuevo', reservacion_view, name = 'crear_reservacion'),
    path('Reservacion/ver', lista_reservacion, name = 'ver_reservacion'),
    path('Reservacion/editar/<idRes>', editar_reservacion, name = 'editar_reservacion'),
    path('Reservacion/eliminar/<idRes>', eliminar_reservacion, name = 'eliminar_reservacion'),    
]
