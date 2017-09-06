from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    # Clase para representar una motocicleta.

    def __init__(self, modelo, color, transmision, motor, cilindros, sku,
    tipo, centimetros_cubicos, existencia=1):
        # Heredamos los atributos de 'Vehiculo'.
        super().__init__(modelo, color, transmision, motor, cilindros, sku)
        # Definimos los atributos particulares de una motocicleta.
        self.tipo = tipo
        self.centimetros_cubicos = centimetros_cubicos

    def get_tipo(self):
        # Regresa el tipo.
        return self.tipo

    def set_tipo(self, tipo):
        # Asigna un tipo.
        self.tipo = tipo

    def get_centimetros_cubicos(self):
        # Regresa cuántos CC posee.
        return self.centimetros_cubicos

    def set_centimetros_cubicos(self, centimetros_cubicos):
        # Asigna un valor de CC.
        self.centimetros_cubicos = centimetros_cubicos

    def get_info_motocicleta(self):
        # Regresa un resumen de la motocicleta.

        info = "Modelo: {}\nColor: {}\nTipo: {}\n".format(self.modelo,
        self.color, self.tipo)
        info += "Transmisión: {}\nMotor: {}\nCilindros: {}\n".format(self.transmision,
        self.motor, self.cilindros)
        info += "CC: {}\nSKU: {}\nExistencia: {}\n".format(self.centimetros_cubicos,
        self.sku, self.existencia)

        return info


'''
mi_moto = Motocicleta('Ducati Monster 1200S 2017', 'Negro', 'Cadena',
'Testastretta 11° L-Twin', 4, 'DUC-MON-1200S-01', 'Urbana', 1198)
print(mi_moto.get_info_motocicleta())
'''
