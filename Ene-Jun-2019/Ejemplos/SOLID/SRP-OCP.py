class Almacen(object):
    """docstring for Almacen"""

    def __init__(self, articulos={}):
        self.articulos = articulos
        self.existencias = {}

    def add_articulo(self, articulo, cantidad=0):
        if articulo.get_categoria() not in self.articulos.keys():
            self.articulos[articulo.get_categoria()] = [articulo]
        else:
            self.articulos[articulo.get_categoria()].append(articulo)

        if articulo.get_sku() not in self.existencias.keys():
            self.existencias[str(articulo.get_sku())] = cantidad
        else:
            self.existencias[str(articulo.get_sku())] += cantidad

    def update_existencia(self, articulo, cantidad):
        self.existencias[str(articulo.get_sku())] -= cantidad

    def __str__(self):
        output = ''

        for categoria, lista_categoria in self.articulos.items():
            output += '### Categoría {} ###\n\n'.format(categoria)
            for articulo in lista_categoria:
                output += '* Artículo *\n{}\nExistencia: {}\n\n'.format(str(articulo), self.existencias[str(articulo.get_sku())])

        return output

class Articulo(object):
    """docstring for Articulo"""

    def __init__(self, **args):
        self.precio = args.get('precio', 0)
        self.sku = args.get('sku', 000000)
        self.categoria = args.get('categoria', '')
        self.nombre = args.get('nombre', '')

    def set_precio(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    def set_sku(self, sku):
        self.sku = sku

    def get_sku(self):
        return self.sku

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def __str__(self):
        return """
            Nombre: {}\nPrecio: {}\nSKU: {}\nCategoría: {}\n
        """.format(self.nombre, self.precio, self.sku, self.categoria).strip()

# Se surte el almacen
articulo = Articulo(
    nombre='pan',
    categoria='alimentos',
    sku=998471,
    precio=10
)

almacen = Almacen()
almacen.add_articulo(articulo, 10)
almacen.add_articulo(Articulo(
    nombre='jugo',
    categoria='alimentos',
    sku=998472,
    precio=15
), 2)

almacen.add_articulo(Articulo(
    nombre='desarmador',
    categoria='herramientas',
    sku=872634,
    precio=25
), 5)

# Se compra un artículo
almacen.update_existencia(articulo, 4)
print(almacen)
