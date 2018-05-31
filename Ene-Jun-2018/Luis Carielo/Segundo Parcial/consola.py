class Consola:
	def __init__(self, id_consola, nombre_consola, precio_consola):
		self.id_consola = id_consola
		self.nombre_consola = nombre_consola
		self.precio_consola = precio_consola

	def __repr__(self):
		return "Consola('{}', '{}', '{}')".format(self.id_consola, self.nombre_consola, self.precio_consola)