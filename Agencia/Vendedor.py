from Persona import Persona
# To-do: -> Agencia

class Vendedor(Persona):
    # Clase para representar a un vendedor.

    def __init__(self, nombre, apellido_paterno, apellido_materno, genero, edad,
    domicilio, telefono, id_vendedor):
        # Heredamos los atributos de 'Persona'.
        super().__init__(nombre, apellido_paterno, apellido_materno, genero, edad,
        domicilio, telefono)
        # Definimos los atributos propios de un vendedor.
        self.id_vendedor = id_vendedor
        self.autos_vendidos = 0

    def get_id_vendedor(self):
        # Regresa el id del vendedor.
        return self.id_vendedor

    def set_id_vendedor(self, id_vendedor):
        # Asigna un id al vendedor.
        self.id_vendedor = id_vendedor

    def get_autos_vendidos(self):
        # Regresa la cantidad de autos vendidos.
        return self.autos_vendidos

    def incrementa_autos_vendidos(self):
        # Incrementa por uno los autos vendidos.
        self.autos_vendidos += 1

    def cumplio_meta(self):
        # Determina si el vendedor cumplió la meta.

        if self.autos_vendidos >= 1:
            goal_info = "El vendedor cumplió la meta establecida."
            goal_info += "\nAutos vendidos: {}".format(self.autos_vendidos)
        else:
            goal_info = "El vendedor no cumplió la meta establecida."
            goal_info += "\nAutos vendidos: {}".format(self.autos_vendidos)

        return goal_info

    def get_info_vendedor(self):
        # Regresa un resumen del vendedor.

        info = "Nombre: {}\nApellido Paterno: {}\nApellido Materno: {}\n".format(self.nombre,
        self.apellido_paterno, self.apellido_materno)
        info += "Genero: {}\nEdad: {}\nDomicilio: {}\n".format(self.genero,
        self.edad, self.domicilio)
        info += "Teléfono: {}\nId del vendedor: {}\nAutos vendidos: {}".format(self.telefono,
        self.id_vendedor, self.autos_vendidos)

        return info


new_vendedor = Vendedor('Juan', 'Perez', 'Gómez', 'M', 28,
'Los Álamos 412 Col. Bosques del Pedregal', '844-123-45-67', 1)
print(new_vendedor.get_info_vendedor())
new_vendedor.incrementa_autos_vendidos()
print(new_vendedor.cumplio_meta())
