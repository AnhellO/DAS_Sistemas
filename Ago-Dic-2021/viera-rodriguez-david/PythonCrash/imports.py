################
#Ejercicio 9-10#
################
# from ejercicios import Restaurante

# terraza = Restaurante('La Terraza', 'Cortes y Mar')
# terraza.descripcion_restaurant()
# terraza.restaurant_abierto()

################
#Ejercicio 9-11#
################
# from ejercicios import Admin

# david = Admin('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
# david.descripcion_usuario()

# david_privilegios = [
#       'Puede hacer reset de contraseñas',
#       'Puede suspender cuentas',
#       'Puede ver historial de cuentas'
#     ]
# david.privilegios.privilegios = david_privilegios

# print("\nEl administrador " + david.usuario + " Tiene estos privilegios: ")
# david.privilegios.muestra_privilegios()

################
#Ejercicio 9-12#
################

from ejercicios import Usuario

class Admin(Usuario):
    """Usuario con privilegios administrador."""

    def __init__(self, nombre, apellido, usuario, email):
        """Inicia admin."""
        super().__init__(nombre, apellido, usuario, email)

        "Inicia un set vacio de privilegios"
        self.privilegios = Privilegios()

class Privilegios():
    "clase para almacenar los privilegios de un administrador"
    def __init__(self, privilegios=[]):
      self.privilegios = privilegios

    def muestra_privilegios(self):
      print("\nPrivilegios de usuario:")
      if self.privilegios:
          for privilegio in self.privilegios:
              print("- " + privilegio)


