
class CafeAbstracto():
	def tipo(self):
		pass

	def precio(self):
		pass

class CafeSimple(CafeAbstracto):
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

    def ingrediente():
        return 'Cafecito con: '

    def precio():
        return 25

    def imprime(self):
        print('Cafecito con {} a solo ${} pesitos!!'.format(self.tipo, self.precio))


if __name__ == '__main__':
    cafecito1 = CafeSimple('Vainilla', 32)
    cafecito2 = CafeSimple('Leche', 28)
    cafecito3 = CafeSimple('Canela', 30)
    cafecito1.imprime()
    cafecito2.imprime()
    cafecito3.imprime()
