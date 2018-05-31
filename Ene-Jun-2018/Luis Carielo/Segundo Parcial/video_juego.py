class VideoJuego:
	def __init__(self, id_videojuego, nombre_videojuego, precio_videojuego):
		self.id_videojuego = id_videojuego
		self.nombre_videojuego = nombre_videojuego
		self.precio_videojuego = precio_videojuego

	def __repr__(self):
		return "VideoJuego('{}', '{}', '{}')".format(self.id_videojuego, self.nombre_videojuego, self.precio_videojuego)