################
#Ejercicio 9-12#
################
from imports import Admin

david = Admin('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
david.descripcion_usuario()

david_privilegios = [
      'Puede hacer reset de contraseñas',
      'Puede suspender cuentas',
      'Puede ver historial de cuentas'
    ]
david.privilegios.privilegios = david_privilegios

print("\nEl administrador " + david.usuario + " Tiene estos privilegios: ")
david.privilegios.muestra_privilegios()