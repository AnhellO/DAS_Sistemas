diccionario = {
    'a': ['accion', 'arte', 'arquitectura', 'agrego', 'actual'],
    'b': ['bueno', 'bien', 'bonito'],
    'c': ['casa', 'clase', 'coctel']
}

diccionario['d'] = ['dado', 'diccionario', 'duda']

# print(diccionario)
# print(diccionario['a'])

for llave, valor in diccionario.items():
    pass #print("sho soy la llavesita -> {}, y el valor es: {}".format(llave, valor))

for llave in diccionario.keys():
    pass #print("sho soy la puro llavesita: {}".format(llave))

for valor in diccionario.values():
    pass #print("sho soy el puro valor: {}".format(valor))

# print(sorted(diccionario.items()))

tupla = (1, 2, 3)
lista = [4, 2, 3]
lista[0] = 0
# print(lista[0])
# print(len(lista))
# print(len(diccionario))
# print(len(diccionario['a']))

class Automovil(object):
    bolsas_de_aire = 0

    """docstring for Automovil"""
    def __init__(self, **argumentos):
        self.llantas = argumentos.get('llantas')
        self.motor = argumentos.get('motor')
        self.transmision = argumentos.get('transmision')
        self.bolsas_de_aire = argumentos.get('bolsas_de_aire', 0)
        self.marca = argumentos.get('marca')

    def set_llantas(self, llantas):
        self.llantas = llantas
        return self

    def set_motor(self, motor):
        self.motor = motor
        return self

    def set_transmision(self, transmision):
        self.transmision = transmision
        return self

    def get_llantas(self):
        return self.llantas

    def get_motor(self):
        return self.motor

    def get_transmision(self):
        return self.transmision

    def __str__(self):
        return """
        Llantas: {}\nMotor: {}\nTransmision: {}\n# de Bolsas de Aire: {}\nMarca: {}
        """.format(self.llantas, self.motor, self.transmision, self.bolsas_de_aire, self.marca).strip().lower()

#auto = Automovil(motor='v8', transmision='estándar')
#auto2 = Automovil(motor='v4')
auto3 = Automovil(motor='v6', llantas='euzkadi', transmision='cvt', marca='honda')
#auto3.set_motor('v6').set_llantas('euzkadi').set_transmision('cvt')
#print(auto.get_motor())
#print(auto.get_transmision())
#print(auto.get_llantas())
#print(auto)
#print(auto2)
print(auto3)
