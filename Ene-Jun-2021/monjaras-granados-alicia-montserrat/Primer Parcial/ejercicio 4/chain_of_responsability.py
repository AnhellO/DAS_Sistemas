import abc

# Interfaz comun a los manejadores concretos
class CajeroHandler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self, cantidad):
        pass

    @abc.abstractmethod
    def next_successor(self):
        pass

  

# Clase base handler (Segmentos de código que no puede alterarse)
class BaseCajeroHandler(CajeroHandler):
    
    def next_successor(self, next_handler: CajeroHandler) -> None:
        self.next = next_handler

    def handle(self, cantidad):
        if self.next != None:
            return self.next.handle(cantidad)


# Manejadores Conretos : procesan el código
class Cajero50ConcreteHandler(BaseCajeroHandler):
    
    def __init__(self):# cosntructor
        # definie el atributo de cuantro valdrá el billete
        self.billete = 50
        
    def handle(self, cantidad): #se utlizo la misma lógica para obtener la cantidad de billetes sehun el valor que tenga el billete en el costructor
        #condiciona que la cantidad de billetes a cambiar sea  menor a 10, que tambien obtiene el resto de la división de los números  sea diferente de 0
        if cantidad < 10 or cantidad % 10 !=0:
            print("No es posible hacer el cambio de billetes")
            return # sale del programa
        #print((f"Cajero50ConcreteHandler {cantidad}")) # define la cantidad que le llega a la clase
        if cantidad >= self.billete:
           cantidad_billetes =  cantidad // self.billete 
           residuo = cantidad %  self.billete
           print(f"Tendras: {cantidad_billetes} billetes de {self.billete}") 
           if residuo != 0: 
                super().handle(residuo)
        else:
            super().handle(cantidad)

# Manejadores Conretos : procesan el código           
class Cajero20ConcreteHandler(BaseCajeroHandler):

   def __init__(self):
        # definie cuantro valdrá el billete
        self.billete = 20

   def handle(self, cantidad) :
        #condiciona que la cantidad de billetes a cambiar sea  menor a 10, que tambien obtiene el resto de la división de los números  sea diferente de 0
        if cantidad < 10 or cantidad % 10 !=0:
            print("No es posible hacer el cambio de billetes")
            return # sale del programa
        #print((f"Cajero20ConcreteHandler {cantidad}")) #define la cantidad que le llega a la clase
        if cantidad >= self.billete:
           cantidad_billetes =  cantidad // self.billete 
           residuo = cantidad %  self.billete
           print(f"Tendras: {cantidad_billetes} billetes de {self.billete}")  
           if residuo != 0:
               super().handle(residuo)
        else:
            super().handle(cantidad)


# Manejadores Conretos : procesan el código
class Cajero10ConcreteHandler(BaseCajeroHandler):

   def __init__(self):
        # definie cuantro valdrá el billete
        self.billete = 10

   def handle(self, cantidad) :
        #condiciona que la cantidad de billetes a cambiar sea  menor a 10, que tambien obtiene el resto de la división de los números  sea diferente de 0
        if cantidad < 10 or cantidad % 10 !=0:
            print("No es posible hacer el cambio de billetes")
            return # sale del programa
        #print((f"Cajero10ConcreteHandler {cantidad}")) #define la cantidad que le llega a la clase
        if cantidad >= self.billete: # condiciona si la cantidad es mayor al billete
           cantidad_billetes =  cantidad // self.billete # cociente de la division  el resultado es un num entero
           residuo = cantidad %  self.billete  #obtiene el resto de la división de los números
           print(f"Tendras: {cantidad_billetes} billetes de {self.billete}") #imprime la cantidad de billetes que puede obtener por la cantidad ingresada
           if residuo != 0: # si el residuo  que es diferente de 0
               super().handle(residuo) #pasa al sig handle pero con el valor del residuo
        else: 
            super().handle(cantidad)#pasa al siguente  handle pero con la cantidad

#  Clase cliente:  declara  la logica de como sera procesada la informacion (nota: no es necesario pasar por el primero)

class CajeroATMChain():

    def __init__(self): # el constructor tiene los siguentes atributos
        #declara los manejadores que existen 
        self.chain1 = Cajero50ConcreteHandler()
        self.chain2 = Cajero20ConcreteHandler()
        self.chain3 = Cajero10ConcreteHandler()
        # define como se usara el manejador
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)




def main():
    # manda a llamar la clase donde se estructuro la cadena
    x = CajeroATMChain() 

    # declara el billete a cambiar
    billete_a_cambiar = int(5) # ejemplo1
    # define por cual manejador  pasará y mostrará la información
    x.chain1.handle(billete_a_cambiar)#ejemplo1
    #x.chain2.handle(billete_a_cambiar_2)

   

if __name__ == "__main__":
    main()



