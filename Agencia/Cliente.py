from Persona import Persona
# To-do: -> Vehiculo(?)

class Cliente(Persona):
    # Clase para representar a un cliente.

    def __init__(self, nombre, apellido_paterno, apellido_materno, genero, edad,
    domicilio, telefono, id_cliente):
        # Heredamos los atributos de 'Persona'.
        super().__init__(nombre, apellido_paterno, apellido_materno, genero, edad,
        domicilio, telefono)
        # Definimos los atributos propios de un cliente.
        self.id_cliente = id_cliente

    def get_id_cliente(self):
        # Regresa el id del cliente.
        return self.id_cliente

    def set_id_cliente(self, id_cliente):
        # Asigna un id al cliente.
        self.id_cliente = id_cliente

    def get_info_cliente(self):
        # Regresa un resumen del cliente.

        info = "Nombre: {}\nApellido Paterno: {}\nApellido Materno: {}\n".format(self.nombre,
        self.apellido_paterno, self.apellido_materno)
        info += "Genero: {}\nEdad: {}\nDomicilio: {}\n".format(self.genero,
        self.edad, self.domicilio)
        info += "Teléfono: {}\nId del cliente: {}".format(self.telefono,
        self.id_cliente)

        return info


new_cliente = Cliente('Juan', 'Perez', 'Gómez', 'M', 28,
'Los Álamos 412 Col. Bosques del Pedregal', '844-123-45-67', 1)
print(new_cliente.get_info_cliente())
