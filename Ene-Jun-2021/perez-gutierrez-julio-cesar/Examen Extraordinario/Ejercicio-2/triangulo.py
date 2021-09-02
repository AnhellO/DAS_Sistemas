from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self, angulo1, angulo2, angulo3, lado1, lado2, lado3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.num_de_lados = 3
    
    def __str__(self):
        return f"Angulo 1 = {self.angulo1}\nAngulo 2 = {self.angulo2}\n" \
                f"Angulo 3 = {self.angulo3}\nLado 1 = {self.lado1}\n" \
                f"Lado 2 = {self.lado2}\nLado 3 = {self.lado3}\nValidar : {self.verificar_triangulo()}" 
    
    def verificar_angulos(self):
        return self.angulo1 + self.angulo2 + self.angulo3 == 180
    
    @abstractmethod
    def verificar_triangulo(self) -> bool:
        pass

class Equilatero(Triangulo):
    def verificar_triangulo(self):
        return self.lado1 == self.lado2 and self.lado2 == self.lado3

class Isoceles(Triangulo):
    def verificar_triangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return False
        elif(self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3):
            return True
        else: return False

class Escaleno(Triangulo):
    def verificar_triangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return False
        elif(self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3):
            return False
        elif (self.lado1 != self.lado2 or self.lado1 != self.lado3 or self.lado2 != self.lado3):
            return True


if __name__ == '__main__':
################_angulos_#_lados_###########
    equilatero = Equilatero(90,60,30,10,10,10)
    iso = Isoceles(90,60,30,10,10,20)
    escaleno = Escaleno(90,60,30,10,20,30)
    print(equilatero.verificar_triangulo())
    print(iso.verificar_triangulo())
    print(escaleno.verificar_triangulo())
