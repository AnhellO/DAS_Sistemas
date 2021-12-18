class Vehiculo:

    random = 1234

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        self.vm = velocidad_maxima
        self.k = kilometraje
        self.c = capacidad
        self.tarifa()
    
    def tarifa(self):
        self.tar = self.c * 100

    def __str__(self):
        cadena = 'Velocidad max: {self.vm}.\nkilometraje: {self.k}.\ncapacidad: {self.c}.\ntarifa: ${self.tar}'.format(self=self)
        return cadena

class Autobus(Vehiculo):
    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        Vehiculo.__init__(self, velocidad_maxima, kilometraje, capacidad)
        self.mFinal

    def mFinal(self):
        self.tar += self.tar*0.1

    def __str__(self):
        cadena = 'Velocidad max: {self.vm}.\nkilometraje: {self.k}.\ncapacidad: {self.c}.\ntarifa: ${self.tar}'.format(self=self)
        return cadena

def main():
    lista = [Vehiculo(100,100,4),Autobus(100,100,40),Autobus(100,100,30),Vehiculo(200,0,2)]

    for obj in lista:
        if isinstance(obj, Autobus):
            print('¡Soy un autobus!\n',obj)

if __name__ == "__main__":
    main()