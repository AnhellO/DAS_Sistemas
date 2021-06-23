from __future__ import annotations
from abc import ABC, abstractmethod

# fabrica
class Factory_Triangulo(ABC):
    @abstractmethod
    def get_triangulo(self) -> Triangulo:
        pass

class ConcreteCreatorEquilatero(Factory_Triangulo):
    def get_triangulo(self, t:Triangulo):         
        return ConcreteProductEquilatero(t.a1, t.a2, t.a3, t.l1, t.l2, t.l3) 
        #instancia del tipo de triangulo

class ConcreteCreatorIsoceles(Factory_Triangulo):
    def get_triangulo(self, t:Triangulo):
        return ConcreteProductIsoceles(t.a1, t.a2, t.a3, t.l1, t.l2, t.l3)

class ConcreteCreatorEscaleno(Factory_Triangulo):
    def get_triangulo(self, t: Triangulo):
        return ConcreteProductEscaleno(t.a1, t.a2, t.a3, t.l1, t.l2, t.l3)

# interface product
class Triangulo(ABC):
    def __init__(self, a1, a2, a3, l1, l2, l3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.num_de_lados = 3
    
    def __str__(self):
        return f"Angulo 1 = {self.a1}\nAngulo 2 = {self.a2}\n" \
                f"Angulo 3 = {self.a3}\nLado 1 = {self.l1}\n" \
                f"Lado 2 = {self.l2}\nLado 3 = {self.l3}\nValidar : {self.verificar_triangulo()}" 
    
    def verificar_angulos(self):
        return self.a1 + self.a2 + self.a3 == 180
    
    @abstractmethod
    def verificar_triangulo(self) -> bool:
        pass

# products A,B,C
class ConcreteProductEquilatero(Triangulo):
    def verificar_triangulo(self):
        return self.l1 == self.l2 and self.l2 == self.l3

class ConcreteProductIsoceles(Triangulo):
    def verificar_triangulo(self):
        if self.l1 == self.l2 and self.l2 == self.l3:
            return False
        elif(self.l1 == self.l2 or self.l1 == self.l3 or self.l2 == self.l3):
            return True
        else: return False

class ConcreteProductEscaleno(Triangulo):
    def verificar_triangulo(self):
        if self.l1 == self.l2 and self.l2 == self.l3:
            return False
        elif(self.l1 == self.l2 or self.l1 == self.l3 or self.l2 == self.l3):
            return False
        elif (self.l1 != self.l2 or self.l1 != self.l3 or self.l2 != self.l3):
            return True

# if __name__ == "__main__":
#     equilatero = ConcreteProductEquilatero(90,60,30,10,10,10)
#     isoceles = ConcreteProductIsoceles(90,60,30,10,10,20)
#     escaleno = ConcreteProductEscaleno(90,60,30,10,20,30)
#     c1 = ConcreteCreatorEquilatero().get_triangulo(equilatero)
#     c2 = ConcreteCreatorIsoceles().get_triangulo(isoceles)
#     c3 = ConcreteCreatorEscaleno().get_triangulo(escaleno)
#     print(c1)
#     print(c2)
#     print(c3)