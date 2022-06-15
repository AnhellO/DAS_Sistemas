from __future__ import annotations
from webSite import *
import abc

'''
Se implementa el praton Proxy para agragar una pequeña capa de autenticación de usuario
y contraseña a distintos tipos de objetos de la clase WebSite
'''

# Interface
class ObjetosInterface(abc.ABC):
    @abc.abstractmethod
    def objetoTipo1(self):
        pass

    @abc.abstractmethod
    def objetoTipo2(self):
        pass

    @abc.abstractmethod
    def objetoTipo3(self):
        pass

class ObjetosWebSite(ObjetosInterface): # Implementa la interface
    def __init__(self) -> None:
        # Atributo de tipo WebSite
        self.wb = WebSite()

    # 'Crea' un tipo de objeto y lo retorna 
    def objetoTipo1(self):
        self.wb.setDominio('amazon')
        self.wb.setSubdominio('www')
        self.wb.setExtension('.com')
        self.wb.setDescripcion('Shopping')
        self.wb.setHosting('Hosting El Mariachi')
        self.wb.setAdaptadoMoviles(True)
        return self.wb
    
    def objetoTipo2(self):        
        self.wb.setDominio('cars.com')
        self.wb.setSubdominio('www')
        return self.wb
    
    def objetoTipo3(self):
        self.wb.setDominio('themeforest.com')
        self.wb.setSubdominio('www')
        self.wb.setDescripcion('Diferentes temas')                
        return self.wb
        
# Clase Proxy, implementa la interface
class ObjetosProxy(ObjetosInterface):
    def __init__(self,usuario : Usuario) -> None:
        # Atributo de tipo ObjetosWebSite
        self.owb = ObjetosWebSite()
        self.usuario = usuario      
        self.tipo = 0

    # Función que permite cambiar de usuario
    def cambiarUsuario(self,usuaio):
        self.usuario = usuaio

    def objetoTipo1(self):
        self.tipo = 1                            
        if self.usuario.contrasena[-1] == '%': # Verifica un tipo de contraseña el cuál si cumple con lo       
            self.mensajeInstancia()            # indicado permite instanciar el tipo de objeto he imprime
            return self.owb.objetoTipo1()      # un mensaje, sino retorna un mensaje de 'error'     
        return self.mensajeError()

    def objetoTipo2(self):
        self.tipo = 2
        if self.usuario.contrasena[0] == '_' and self.usuario.contrasena[-1] == '%':            
            self.mensajeInstancia()
            return self.owb.objetoTipo2()            
        return self.mensajeError()

    def objetoTipo3(self):
        self.tipo = 3
        if (self.usuario.contrasena[0] and self.usuario.contrasena[1]) == '&':            
            self.mensajeInstancia()
            return self.owb.objetoTipo3()            
        return self.mensajeError()        

    def mensajeInstancia(self):
        print(f"Se ha instanciado un objeto de tipo: {self.tipo}")

    def mensajeError(self):
        return f"El usuario {self.usuario.nombre} no puede instanciar un objeto de tipo: {self.tipo}"

class Usuario():    # Clase usuario
    def __init__(self,nombre,contrasena) -> None:
        self.nombre = nombre        
        self.contrasena = contrasena

# Cliente
def main():
    # Se crea objeto tipo Usuario
    usuario1 = Usuario('Pedro', 'hsd3864%')    
    oProxy = ObjetosProxy(usuario1)  # Objeto de tipo ObjetosProxy, que se le encia el usuario

    objt1 = oProxy.objetoTipo1()
    print(objt1)
    objt2 = oProxy.objetoTipo2()
    print(objt2)        
    objt3 = oProxy.objetoTipo3()
    print(objt3)
    '''
    Se ha instanciado un objeto de tipo: 1
    <webSite.WebSite object at 0x7f88fceba1c0>
    El usuario Pedro no puede instanciar un objeto de tipo: 2
    El usuario Pedro no puede instanciar un objeto de tipo: 3
    '''   

    print()
    usuario2 = Usuario('Perla', '_elsapito%')
    oProxy.cambiarUsuario(usuario2) # Se cambia el usuario
    objt1 = oProxy.objetoTipo1()
    print(objt1)
    objt2 = oProxy.objetoTipo2()
    print(objt2)        
    objt3 = oProxy.objetoTipo3()
    print(objt3)

    '''
    Se ha instanciado un objeto de tipo: 1
    <webSite.WebSite object at 0x7f2a50c2b1c0>
    Se ha instanciado un objeto de tipo: 2
    <webSite.WebSite object at 0x7f2a50c2b1c0>
    El usuario Perla no puede instanciar un objeto de tipo: 3
    '''

    print()
    usuario3 = Usuario('Luis', '&&taquito%')
    oProxy.cambiarUsuario(usuario3)
    objt1 = oProxy.objetoTipo1()
    print(objt1)
    objt2 = oProxy.objetoTipo2()
    print(objt2)        
    objt3 = oProxy.objetoTipo3()
    print(objt3)

    '''
    Se ha instanciado un objeto de tipo: 1
    <webSite.WebSite object at 0x7f6dc01301c0>
    El usuario Luis no puede instanciar un objeto de tipo: 2
    Se ha instanciado un objeto de tipo: 3
    <webSite.WebSite object at 0x7f6dc01301c0>
    '''


if __name__ == '__main__':
    main()