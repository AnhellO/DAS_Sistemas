from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    # Clase para representar un automóvil.

    def __init__(self, modelo, color, transmision, motor, cilindros, sku,
    puertas, equipado, rendimiento, carroceria, existencia=1):
        # Heredamos los atributos de 'Vehiculo'.
        super().__init__(modelo, color, transmision, motor, cilindros, sku)
        # Definimos los atributos particulares de un automóvil.
        self.puertas = puertas
        self.equipado = equipado
        self.rendimiento = rendimiento
        self.carroceria = carroceria

    def get_puertas(self):
        # Regresa el número de puertas.
        return self.puertas

    def set_puertas(self, puertas):
        # Asigna un número de puertas.
        self.puertas = puertas

    def get_equipado(self):
        # Regresa si el automóvil es equipado o no.
        return self.equipado

    def set_equipado(self, equipado):
        # Asigna un valor de equipación al automóvil.
        self.equipado = equipado

    def get_rendimiento(self):
        # Regresa el valor del rendimiento km/L.
        return rendimiento

    def set_rendimiento(self, rendimiento):
        # Asigna un valor de rendimiento km/L.
        self.rendimiento = rendimiento

    def get_carroceria(self):
        # Regresa el tipo de carrocería.
        return carroceria

    def set_carroceria(self, carroceria):
        # Asigna un tipo de carrocería.
        self.carroceria = carroceria

    def get_info_automovil(self):
        # Regresa un resumen del automóvil.

        info = "Modelo: {}\nColor: {}\nPuertas: {}\n".format(self.modelo,
        self.color, self.puertas)
        info += "Transmisión: {}\nMotor: {}\nCilindros: {}\n".format(self.transmision,
        self.motor, self.cilindros)
        info += "Equipado: {}\nSKU: {}\nRendimiento: {}km/L\n".format(self.equipado,
        self.sku, self.rendimiento)
        info += "Carrocería: {}\nExistencia: {}\n".format(self.carroceria,
        self.existencia)

        return info


'''
mi_auto = Automovil('Ford Focus S 2017', 'Rojo', 'Automático', '2.0L',
'4', 'FRD-FC-S-17', 5, True, 15, 'Hatchback')
print(mi_auto.get_info_automovil())
mi_auto.set_transmision("Manual")
print(mi_auto.get_info_automovil())
'''
