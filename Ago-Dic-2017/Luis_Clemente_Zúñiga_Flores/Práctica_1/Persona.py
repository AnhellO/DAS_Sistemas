
class Persona:
    """Abstract class Persona
    """
    # Attributes:
    __nombre = ""  # (String) 
    __apellidoPaterno = ""  # (String) 
    __apellidoMaterno = ""  # (String) 
    __domicilio = ""  # (String) 
    __edad = 0  # (int) 
    __genero = ""  # (String) 
    __telefono = ""  # (String) 
    
     # Operations
    
    def __init__(self,nombre,paterno,materno,edad,genero,direccion,telefono):
        self.__nombre = nombre
        self.__apellidoPaterno = paterno
        self.__apellidoMaterno = materno
        self.__edad = edad
        self.__genero = genero
        self.__direccion = direccion
        self.__telefono = telefono
        
   
    def estableceNombre(self, nombre):
        self.__nombre = nombre
        
    def obtenNombre(self):
        return self.__nombre
    
    def estableceApellidoPaterno(self, paterno):
        self.__apellidoPaterno = paterno
      
    def obtenApellidoPaterno(self):
        return self.__apellidoPaterno
    
    def estableceApellidoMaterno(self, materno):
        self.__apellidoMaterno = materno
    
    def obtenApellidoMaterno(self):
        return self.__apellidoMaterno
        
    def estableceDireccion(self, direccion):
        self.__direccion = direccion

    
    def obtenDireccion(self):
        return self.__direccion
        
    def estableceTelefono(self, telefono):
        self.__telefono = telefono
    def obtenTelefono(self):
        return self.__telefono
        
    def estableceEdad(self, edad):
        self.__edad = edad
    
    def obtenEdad(self):
        return self.__edad
        
    def estableceGenero(self, genero):
        self.__genero = genero
        
    def obtenGenero(self):
        return self.__genero

