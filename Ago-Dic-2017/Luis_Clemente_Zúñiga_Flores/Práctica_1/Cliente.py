from Persona import Persona

class Cliente(Persona):
    """Class Cliente
    """
    # Attributes:
    __numeroDeCliente = ""  # (String)

    # Operations
    def __init__(self,nombre,paterno,materno,edad,genero,direccion,telefono,numCli):
        super().__init__(nombre,paterno,materno,edad,genero,direccion,telefono)
        self.__numeroDeCliente = numCli

    def setNumeroDeCliente(self, numCli):
       self.__numeroDeCliente = numCli

    def getNumeroDeCliente(self):
        return self.__numeroDeCliente

    def datosDeCliente(self):		
        datos_cliente = 'Datos del cliente:\n'
        datos_cliente+= 'Nombre:\n'
        datos_cliente+= super(Cliente,self).getNombre()
        datos_cliente+= ' '
        datos_cliente+= super(Cliente,self).getApellidoPaterno()
        datos_cliente+= ' '
        datos_cliente+= super(Cliente,self).getApellidoMaterno() + '\n'
        datos_cliente+= 'Número de cliente:\n'
        datos_cliente+= str(self.getNumeroDeCliente()) + '\n'
        datos_cliente+= 'Edad:\n'
        datos_cliente+= super(Cliente,self).getEdad() + '\n'
        datos_cliente+= 'Dirección:\n'
        datos_cliente+= super(Cliente,self).getDireccion() + '\n'
        datos_cliente+= 'Género:\n'
        datos_cliente+= super(Cliente,self).getGenero() + '\n'
        datos_cliente+= 'Teléfono:\n'
        datos_cliente+= super(Cliente,self).getTelefono() + '\n'
        return datos_cliente

