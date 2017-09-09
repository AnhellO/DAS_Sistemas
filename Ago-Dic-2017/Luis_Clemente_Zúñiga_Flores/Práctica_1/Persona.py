
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
        
   
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setApellidoPaterno(self, paterno):
        self.__apellidoPaterno = paterno
      
    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    
    def setApellidoMaterno(self, materno):
        self.__apellidoMaterno = materno
    
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
        
    def setDireccion(self, direccion):
        self.__direccion = direccion

    
    def getDireccion(self):
        return self.__direccion
        
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def getTelefono(self):
        return self.__telefono
        
    def setEdad(self, edad):
        self.__edad = edad
    
    def getEdad(self):
        return self.__edad
        
    def setGenero(self, genero):
        self.__genero = genero
        
    def getGenero(self):
        return self.__genero

