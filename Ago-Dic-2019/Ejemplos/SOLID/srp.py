import sys

class Articulo(object):
	"""docstring for Articulo"""
	def __init__(self, **args):
		self._sku = args.get('sku')
		self._categoria = args.get('categoria')
		self._existencias = args.get('existencias', 0)

	def set_sku(self, sku):
		self._sku = sku

	def get_sku(self):
		return self._sku

	def set_categoria(self, categoria):
		self._categoria = categoria

	def get_categoria(self):
		return self._categoria

	def set_existencias(self, existencias):
		self._existencias = existencias

	def get_existencias(self):
		return self._existencias

	def __str__(self):
		return 'SKU: {}\nCategoría: {}\nExistencias: {}\n'.format(
				self._sku,
				self._categoria,
				self._existencias
			)


class Inventario(object):
	"""docstring for Inventario"""

	_articulos = {}

	def __init__(self, articulos):
		self._articulos = dict(zip(
			[articulo.get_sku() for articulo in articulos],
			articulos
		))

	def get_articulos(self):
		return self._articulos

	def agrega_nuevo_articulo(self, articulo):
		self._articulos[articulo.get_sku()] = articulo

	def modifica_existencias(self, sku, op, cantidad=1):
		if sku not in self._articulos.keys():
			print('Articulo {} no existe!'.format(sku))
			return

		articulo = self._articulos[sku]
		if op == True:
			articulo.set_existencias(articulo.get_existencias() + cantidad)
		
		articulo.set_existencias(articulo.get_existencias() - cantidad)

	def notifica(self, sku, existencia=2):
		if sku in self._articulos.keys() and self._articulos[sku].get_existencias() <= existencia:
			return 'Ya surte artículo {}'.format(sku)

		return 'Existencias al día [{}] para artículo {}'.format(
			self._articulos[sku].get_existencias(),
			self._articulos[sku].get_sku()
		)
		

art = Articulo(sku='1793412')
art.set_categoria('electrónicos')
art.set_existencias(10)

inv = Inventario([art])
inv.agrega_nuevo_articulo(Articulo(sku='101u20e0', categoria='domesticos', existencias=5))
inv.agrega_nuevo_articulo(Articulo(sku='19h29nv9', categoria='mascotas', existencias=25))
# print(inv.get_articulos())
inv.modifica_existencias('1793412', True)
inv.modifica_existencias('1793412', False, 5)

print(art)
print(inv.notifica('101u20e0', 4))


