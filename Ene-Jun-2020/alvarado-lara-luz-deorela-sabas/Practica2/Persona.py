class Persona(object):
    #CONSTRUCTOR
    def __init__(self, nombre, edad, peso, estatura, pasatiempo):

        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.pasatiempo = pasatiempo

    #Get & Set
    def set_nombre(self, nombre):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    def set_edad(self, edad):
        self.edad = edad
    def get_edad(self):
        return self.edad
    def set_peso(self, peso):
        self.edad = peso
    def get_peso(self):
        return self.peso
    def set_estatura(self, estatura):
        self.estatura = estatura
    def get_estatura(self):
        return self.estatura
    def set_pasatiempo(self, pasatiempo):
        self.pasatiempo = pasatiempo
    def get_pasatiempo(self):
        return self.pasatiempo
    #FUNCION INDICE DE MASA CORPORAL
    def imc(self,estatura, peso):
        resultado = (peso/(estatura ** 2))
        return print('IMC: ' + str(resultado))
    #STRING
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad} años\nPeso:{self.peso} kg\nEstatura:{self.estatura} cm\nPasatiempo:{self.pasatiempo}'
#OBJETO
"""
persona = Persona(nombre='Jose Madero', edad='40', peso='85', estatura='1.60', pasatiempo = 'Leer')
print(persona)
persona.imc(peso=85, estatura=1.60)

"""
