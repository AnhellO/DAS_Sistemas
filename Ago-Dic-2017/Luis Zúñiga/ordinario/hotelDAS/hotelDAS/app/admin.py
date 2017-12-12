from django.contrib import admin
from app.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'paterno','materno','email','direccion','edad','tcredito']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['nombre','direccion','estrellas']

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['tipo','idHotel', 'cantidad']
    
class ReservacionAdmin(admin.ModelAdmin):
    model = Reservacion
    list_display = ['numeroReservacion','totalAPagar','tcredito' ,'cantidadNoches']    
    def tcredito(self,obj):
        print(obj)
        return obj.tcredito.tcredito
    tcredito.admin_order_field = 'tcredito'
    tcredito.short_description = 'Tarjeta de crédito'
   


class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ['tipo','precio']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
