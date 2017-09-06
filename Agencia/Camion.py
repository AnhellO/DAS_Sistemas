from Vehiculo import Vehiculo

class Camion(Vehiculo):
    # Clase para representar un camión.

    def __init__(self, modelo, color, transmision, motor, cilindros, sku,
    ejes, capacidad, existencia=1):
        # Heredamos los atributos de 'Vehiculo'.
        super().__init__(modelo, color, transmision, motor, cilindros, sku)
        # Definimos los atributos propios de un camión.
        self.ejes = ejes
        self.capacidad = capacidad

    def get_ejes(self):
        # Regresa el número de ejes.
        return self.ejes

    def set_ejes(self, ejes):
        # Asigna un número de ejes.
        self.ejes = ejes

    def get_capacidad(self):
        # Regresa cuánta capacidad posee.
        return self.capacidad

    def set_capacidad(self, capacidad):
        # Asigna un valor de capacidad.
        self.capacidad = capacidad

    def get_info_camion(self):
        # Regresa un resumen del camión.

        info = "Modelo: {}\nColor: {}\nEjes: {}\n".format(self.modelo,
        self.color, self.ejes)
        info += "Transmisión: {}\nMotor: {}\nCilindros: {}\n".format(self.transmision,
        self.motor, self.cilindros)
        info += "Capacidad: {}\nSKU: {}\n".format(self.capacidad,
        self.sku)

        return info


'''
mi_camion = Camion('Scania R730', 'Rojo', 'Scania GRSO905R',
'Scania DC16 500 16Litre 90° V8', 6, 'SCA-R730-01', 2, '19 toneladas')
print(mi_camion.get_info_camion())
'''
