class Empleado(object):
    puesto = ""

    def factory(clase):
        if clase == "Maestro":
            return Maestro()
        elif clase == "Vendedor":
            return Vendedor()
        elif clase == "Repatidor":
            return Repartidor()


class Maestro(Empleado):
    puesto = "Maestro"

    def mensaje(self):
        return "Hola soy un Maestro"

class Vendedor(Empleado):
    puesto = "Vendedor"

    def mensaje(self):
        return "Hola soy un Vendedor"

class Repartidor(Empleado):
    puesto = "Repartidor"

    def mensaje(self):
        return "Hola soy un Repartidor"


'''Entrada'''
vend = Empleado.factory('Vendedor')
print("Clase: {0}\n{1}".format(vend.puesto, vend.mensaje()))

'''
    Salida Esperada:

            Clase: Vendedor
            Hola soy un Vendedor
'''
