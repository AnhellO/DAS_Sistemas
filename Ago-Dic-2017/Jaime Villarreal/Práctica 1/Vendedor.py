from Persona import Persona
from Vehiculo import Vehiculo

class Vendedor(Persona):
    # Clase para representar a un vendedor.

    def __init__(self, nombre, apellido_paterno, apellido_materno, genero, edad,
    domicilio, telefono, experiencia):
        # Heredamos los atributos de 'Persona'.
        super().__init__(nombre, apellido_paterno, apellido_materno, genero, edad,
        domicilio, telefono)
        # Definimos los atributos propios de un vendedor.
        self.experiencia = experiencia
        self.vehiculos_vendidos = 0

    def get_experiencia(self):
        # Regresa los años de experiencia del vendedor.
        return self.id_vendedor

    def set_experiencia(self, experiencia):
        # Asigna años de experiencia al vendedor.
        self.experiencia = experiencia

    def get_vehiculos_vendidos(self):
        # Regresa la cantidad de vehículos vendidos.
        return self.vehiculos_vendidos

    def incrementa_vehiculos_vendidos(self):
        # Incrementa por uno los vehiculos_vendidos vendidos.
        self.vehiculos_vendidos += 1

    def cumplio_meta(self):
        # Determina si el vendedor cumplió la meta.

        if self.vehiculos_vendidos >= 3:
            goal_info = "\nEl vendedor cumplió la meta establecida."
            goal_info += "\nVehículos vendidos: {}\n".format(self.vehiculos_vendidos)
        else:
            goal_info = "\nEl vendedor no ha cumplido la meta establecida."
            goal_info += "\nVehículos vendidos: {}\n".format(self.vehiculos_vendidos)

        return goal_info

    def get_info_vendedor(self):
        # Regresa un resumen del vendedor.

        info = "Nombre: {}\nApellido Paterno: {}\nApellido Materno: {}\n".format(self.nombre,
        self.apellido_paterno, self.apellido_materno)
        info += "Genero: {}\nEdad: {}\nDomicilio: {}\n".format(self.genero,
        self.edad, self.domicilio)
        info += "Teléfono: {}\nAños de experiencia: {}\nVehículos vendidos: {}".format(self.telefono,
        self.experiencia, self.vehiculos_vendidos)

        return info


'''
new_vendedor = Vendedor('Juan', 'Perez', 'Gómez', 'M', 28,
'Los Álamos 412 Col. Bosques del Pedregal', '844-123-45-67', 1)
print(new_vendedor.get_info_vendedor())
new_vendedor.incrementa_vehiculos_vendidos()
print(new_vendedor.cumplio_meta())
'''
