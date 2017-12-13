from django.contrib import admin
from apps.hotel.models import Cliente, Habitacion, Reservacion

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Reservacion)
