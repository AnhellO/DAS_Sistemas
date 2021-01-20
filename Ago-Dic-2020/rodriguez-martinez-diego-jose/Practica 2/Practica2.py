import random
import math

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre.title()
        self.edad = edad

        self.vida = math.floor(random.random()*100)
        self.vivo = True

    def __str__(self):
        return f'''\nNombre: {self.nombre}\nEdad: {self.edad}\nVida: {self.vida}'''

    def descansa(self):
        if self.vivo:
            aumento = math.floor(random.uniform(1, 100))
            self.vida += aumento

            print(f'{self.nombre} descanso y recupero {aumento} de vida')
        else:
            print(f'{self.nombre} descansara por toda la eternidad')

    def saluda(self):
        if self.vivo:
            return f"Hola, soy {self.nombre}"
        
        return f"'~~  BOOOOOOO  ~~'"

    def hablar(self,persona):
        return f"Buenos dias, {persona.nombre}. Yo {self.nombre} te deseo buenos dias"

#########
#########

class Peleador(Persona):

    __maxdmg = 70

    def __init__(self, nombre, edad, poder = 0):
        super().__init__(nombre, edad)

        if poder and poder > self.__maxdmg:
            self.poder = poder
        else:
            self.poder = math.floor(random.uniform(0,self.__maxdmg))

    def saluda(self):
        if self.vivo:
            print(super().saluda())
            return f"Soy peleador, con poder de {self.poder}"
        
        return super().saluda()

    def __str__(self):
        return super().__str__() + f"\nPoder: {self.poder}"

    def atacar(self,persona):
        persona.vida -= self.poder
        print(f"{self.nombre} ataco a {persona.nombre} quitandole {self.poder} de vida")

        if isinstance(persona, Peleador):
            self.vida -= persona.poder
            print(f"{persona.nombre} ataco devuelta a {self.nombre} quitandole {persona.poder} de vida")

        if self.vida <= 0:
            self.vivo = False
        if persona.vida <=0:
            persona.vivo = False

    def entrenar(self):
        if not self.vivo:
            print(f"RIP")
            return

        if self.poder < self.__maxdmg:
            self.poder += math.floor(random.uniform(0,self.__maxdmg-self.poder))
            print(f"{self.nombre} a aumentado su poder")
        else:
            print(f"{self.nombre} se ha convertido en un ser humano fisicamente perfecto")

############

persona1 = Persona("Pericolo",60)
persona1.saluda()
print(str(persona1))
persona1.descansa()
print("vida:", persona1.vida)

print("#########\n")

#########
jotaro = Peleador("Jotaro",15)
jotaro.saluda()
print(jotaro.hablar(persona1))
print(str(jotaro))
jotaro.entrenar()
print("poder:", jotaro.poder)

while persona1.vida > 0:
    jotaro.atacar(persona1)
    print("vida Pericolo:", persona1.vida)

persona1.descansa()
print(persona1.saluda())
########
print("#########\n")

dio = Peleador("Dio",120)

while dio.vivo and jotaro.vivo:
    dio.atacar(jotaro)

print("vida Jotaro:", jotaro.vida)
print("vida Jotaro:", dio.vida)

print(dio.saluda())
print(jotaro.saluda())