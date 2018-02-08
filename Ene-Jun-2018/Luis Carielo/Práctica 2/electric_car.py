class Carro():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.lectura_odometro = 0

    def get_nombre_descriptivo(self):
        nombre_extendido = str(self.año) + ' ' + self.marca + ' ' + self.modelo
        return nombre_extendido.title()

    def leer_odometro(self):
        print("Este carro tiene " + str(self.lectura_odometro) + " millas recorridas.")

    def actualizar_odometro(self, kilometraje):
        if kilometraje >= self.lectura_odometro:
            self.lectura_odometro = kilometraje
        else:
            print("No puedes regresar el odómetro.")

    def incrementar_odometro(self, millas):
        self.lectura_odometro += millas

class Bateria():
    def __init__(self, tamaño_bateria=70):
        self.tamaño_bateria = tamaño_bateria
    
    def describe_bateria(self):
        print("Este carro tiene una carga de " + str(self.tamaño_bateria) + "-kWh.")

    def get_rango(self):
        if self.tamaño_bateria == 70:
            rango = 240
        elif self.tamaño_bateria == 85:
            rango = 270
        mensaje = "Este carro puede recorrer apróximadamente " + str(rango) + " millas."
        print(mensaje)
    
    def actualizar_bateria(self):
        if self.tamaño_bateria == 70:
            self.tamaño_bateria = 85

class CarroElectrico(Carro):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        #self.tamaño_bateria = 70
        self.bateria = Bateria()

    #def describe_bateria(self):
    #    print("Este carro tiene una carga de " + str(self.tamaño_bateria) + "-kWh.")

    def tanque_gas(self):
        print("Este carro no necesita tanque de gasolina.")

mi_carro = CarroElectrico('tesla', 'model s', 2016)
print(mi_carro.get_nombre_descriptivo())
mi_carro.bateria.describe_bateria()
mi_carro.bateria.get_rango()
mi_carro.bateria.actualizar_bateria()
mi_carro.bateria.describe_bateria()
mi_carro.bateria.get_rango()