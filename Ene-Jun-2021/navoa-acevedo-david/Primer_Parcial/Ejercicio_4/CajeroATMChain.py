#importacion de las clases que ayudaran a nuestro cajeroATM
from Cajero10ConcreteHandler import cajero10
from Cajero20ConcreteHandler import cajero20
from Cajero50ConcreteHandler import cajero50 

class CajeroATM:

    #construccion de atributos de la cadena.   
    def __init__(self):
        self.chain1 = cajero50()
        self.chain2 = cajero20()
        self.chain3 = cajero10() 

        #inicio de cadena y acomodo de billetes/cadena en orden (50>20>10)
        self.chain1.next_sucesor(self.chain2)
        self.chain2.next_sucesor(self.chain3)