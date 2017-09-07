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

    def estableceNumeroDeCliente(self, numCli):
       self.__numeroDeCliente = numCli

    def obtenNumeroDeCliente(self):
        return self.__numeroDeCliente

    def datosDeCliente(self):		
        datos_cliente = 'Datos del cliente:\n'
        datos_cliente+= 'Nombre:\n'
        datos_cliente+= super(Cliente,self).obtenNombre()
        datos_cliente+= ' '
        datos_cliente+= super(Cliente,self).obtenApellidoPaterno()
        datos_cliente+= ' '
        datos_cliente+= super(Cliente,self).obtenApellidoMaterno() + '\n'
        datos_cliente+= 'Número de cliente:\n'
        datos_cliente+= str(self.obtenNumeroDeCliente()) + '\n'
        datos_cliente+= 'Edad:\n'
        datos_cliente+= super(Cliente,self).obtenEdad() + '\n'
        datos_cliente+= 'Dirección:\n'
        datos_cliente+= super(Cliente,self).obtenDireccion() + '\n'
        datos_cliente+= 'Género:\n'
        datos_cliente+= super(Cliente,self).obtenGenero() + '\n'
        datos_cliente+= 'Teléfono:\n'
        datos_cliente+= super(Cliente,self).obtenTelefono() + '\n'
        return datos_cliente

