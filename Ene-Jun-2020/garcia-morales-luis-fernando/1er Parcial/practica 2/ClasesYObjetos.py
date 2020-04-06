import sys
############### PARTE 1########################################33
class Persona(object):
    """docstring for Persona."""
    def __init__(self, **atr):
        self.Nombre = atr.get('Nombre')
        self.Apellidos= atr.get('Apellidos')
        self.Edad= atr.get('Edad')
        self.Peso= atr.get('Peso')
        self.Estatura= atr.get('Estatura')

    def get_Nombre(self):
        return self.Nombre
    def set_Nombre(self, Nombre):
        self.Nombre = Nombre

    def get_Apellidos(self):
        return self.Apellidos
    def set_Apellidos(self, Apellidos):
        self.Nombre =  Apellidos
    def get_Edad(self):
        return self.Edad
    def set_Edad(self, Edad):
        self.Edad = Edad
    def get_Peso(self):
        return self.Peso
    def set_Peso(self, Peso):
        self.Peso = Peso
    def get_Estatura(self):
        return self.Estatura
    def set_Peso(self, Estatura):
        selfEstatura = Estatura    
    
    def __str__(self):
        return f"Nombre: {self.Nombre} \nApellidos: {self.Apellidos} \nEdad: {self.Edad} \nEstatura: {self.Estatura} \nPeso: {self.Peso}"

    def obtener_IMC(self):
        return 'IMC es: '+str(self.Peso/self.Estatura**2)

persona = Persona(Nombre='Emilio',Apellidos='Barrera', Edad=22, Peso=70, Estatura=1.82)
print(persona)
print('---------------------------------------------------------------')