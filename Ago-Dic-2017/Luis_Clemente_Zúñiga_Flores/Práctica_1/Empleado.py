from Persona import Persona

class Empleado(Persona):
    """Class Empleado
    """
    # Attributes:
    __numeroDeEmpleado = 0

    def __init__(self,nombre,paterno,materno,edad,genero,direccion,telefono,numEmp):
        super().__init__(nombre,paterno,materno,edad,genero,direccion,telefono)
        self.__numeroDeEmpleado = numEmp

    # Operations
    def estableceNumeroDeEmpleado(self, numEmp):
       self.__numeroDeEmpleado = numEmp

    def obtenNumeroDeEmpleado(self):
        return self.__numeroDeEmpleado

    def datosDeEmpleado(self):
        datos_empleado = 'Datos del empleado:\n'
        datos_empleado+= 'Nombre:\n'
        datos_empleado+= super(Empleado,self).obtenNombre()
        datos_empleado+= ' '
        datos_empleado+= super(Empleado,self).obtenApellidoPaterno()
        datos_empleado+= ' '
        datos_empleado+= super(Empleado,self).obtenApellidoMaterno() + '\n'
        datos_empleado+= 'Número de empleado:\n'
        datos_empleado+= str(self.obtenNumeroDeEmpleado()) + '\n'
        datos_empleado+= 'Edad:\n'
        datos_empleado+= super(Empleado,self).obtenEdad() + '\n'
        datos_empleado+= 'Dirección:\n'
        datos_empleado+= super(Empleado,self).obtenDireccion() + '\n'
        datos_empleado+= 'Género:\n'
        datos_empleado+= super(Empleado,self).obtenGenero() + '\n'
        datos_empleado+= 'Teléfono:\n'
        datos_empleado+= super(Empleado,self).obtenTelefono() + '\n'	
        return datos_empleado


