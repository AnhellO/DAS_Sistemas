class Persona:
    # Clase para representar a una persona.

    def __init__(self, nombre, apellido_paterno, apellido_materno, genero, edad,
    domicilio, telefono):
        # Inicializa los atributos para describir a una persona.
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def get_nombre(self):
        # Regresa el nombre.
        return self.nombre

    def set_nombre(self, nombre):
        # Asigna un nombre.
        self.nombre = nombre

    def get_apellido_paterno(self):
        # Regresa el apellido paterno.
        return self.apellido_paterno

    def set_apellido_paterno(self, apellido_paterno):
        # Asigna un apellido paterno.
        self.apellido_paterno = apellido_paterno

    def get_apellido_materno(self):
        # Regresa el apellido materno.
        return self.apellido_materno

    def set_apellido_materno(self, apellido_materno):
        # Asigna un apellido materno.
        self.apellido_materno = apellido_materno

    def get_genero(self):
        # Regresa el genero.
        return self.genero

    def set_genero(self, genero):
        # Asigna un genero.
        self.genero = genero

    def get_edad(self):
        # Regresa la edad.
        return self.edad

    def set_edad(self, edad):
        # Asigna una edad.
        self.edad = edad

    def get_domicilio(self):
        # Regresa el domicilio.
        return self.domicilio

    def set_domicilio(self, domicilio):
        # Asigna un domicilio.
        self.domicilio = domicilio

    def get_telefono(self):
        # Regresa el teléfono.
        return self.telefono

    def set_telefono(self, telefono):
        # Asigna un telefono.
        self.telefono = telefono

    def get_info_persona(self):
        # Regresa un resumen de una persona.

        info = "Nombre: {}\nApellido Paterno: {}\nApellido Materno: {}\n".format(self.nombre,
        self.apellido_paterno, self.apellido_materno)
        info += "Genero: {}\nEdad: {}\nDomicilio: {}\n".format(self.genero,
        self.edad, self.domicilio)
        info += "Teléfono: {}".format(self.telefono)

        return info


'''
new_persona = Persona('Juan', 'Perez', 'Gómez', 'M', 28,
'Los Álamos 412 Col. Bosques del Pedregal', '844-123-45-67')
print(new_persona.get_info_persona())
'''
