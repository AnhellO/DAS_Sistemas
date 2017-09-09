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
    def setNumeroDeEmpleado(self, numEmp):
       self.__numeroDeEmpleado = numEmp

    def getNumeroDeEmpleado(self):
        return self.__numeroDeEmpleado

    def datosDeEmpleado(self):
        datos_empleado = 'Datos del empleado:\n'
        datos_empleado+= 'Nombre:\n'
        datos_empleado+= super(Empleado,self).getNombre()
        datos_empleado+= ' '
        datos_empleado+= super(Empleado,self).getApellidoPaterno()
        datos_empleado+= ' '
        datos_empleado+= super(Empleado,self).getApellidoMaterno() + '\n'
        datos_empleado+= 'Número de empleado:\n'
        datos_empleado+= str(self.getNumeroDeEmpleado()) + '\n'
        datos_empleado+= 'Edad:\n'
        datos_empleado+= super(Empleado,self).getEdad() + '\n'
        datos_empleado+= 'Dirección:\n'
        datos_empleado+= super(Empleado,self).getDireccion() + '\n'
        datos_empleado+= 'Género:\n'
        datos_empleado+= super(Empleado,self).getGenero() + '\n'
        datos_empleado+= 'Teléfono:\n'
        datos_empleado+= super(Empleado,self).getTelefono() + '\n'	
        return datos_empleado


