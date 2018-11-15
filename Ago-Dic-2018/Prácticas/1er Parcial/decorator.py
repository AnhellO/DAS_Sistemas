class CafeAbstracto:
	def precio(self):
		pass

	def tipo(self):
		pass

class CafeSimple(CafeAbstracto):
	def precio(self):
		return 25

	def tipo(self):
		return 'Cafecito!'

if __name__ == '__main__':
    cafecito = CafeSimple()
    print(cafecito.tipo())