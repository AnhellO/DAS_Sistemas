from Persona import Persona
# To-do: -> Vehiculo(?)

class Cliente(Persona):
    # Clase para representar a un cliente.

    def __init__(self, nombre, apellido_paterno, apellido_materno, genero, edad,
    domicilio, telefono, email):
        # Heredamos los atributos de 'Persona'.
        super().__init__(nombre, apellido_paterno, apellido_materno, genero, edad,
        domicilio, telefono)
        # Definimos los atributos propios de un cliente.
        self.email = email

    def get_email(self):
        # Regresa el email del cliente.
        return self.email

    def set_email(self, email):
        # Asigna un id al cliente.
        self.email = email

    def get_info_cliente(self):
        # Regresa un resumen del cliente.

        info = "Nombre: {}\nApellido Paterno: {}\nApellido Materno: {}\n".format(self.nombre,
        self.apellido_paterno, self.apellido_materno)
        info += "Genero: {}\nEdad: {}\nDomicilio: {}\n".format(self.genero,
        self.edad, self.domicilio)
        info += "Teléfono: {}\nEmail: {}".format(self.telefono,
        self.email)

        return info



'''
new_cliente = Cliente('Juan', 'Perez', 'Gómez', 'M', 28,
'Los Álamos 412 Col. Bosques del Pedregal', '844-123-45-67', 1)
print(new_cliente.get_info_cliente())
'''
