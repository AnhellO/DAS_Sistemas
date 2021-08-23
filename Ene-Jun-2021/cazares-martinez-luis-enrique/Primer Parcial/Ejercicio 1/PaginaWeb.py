# Se crea la clase con sus respectivos atributos
class PaginaWeb:

    def __init__(self, url, ruta, formato, contenido, titulo, slug, meta_tags):
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.meta_tagas = meta_tags

# Se crea metodo en el cual a traves del titulo se regresa la informacion "Slugificada"
    def slugificar(self, slug):
        min = slug.lower()
        slugificado = min.replace(" ", "-")

        return slugificado

    def __str__(self):
        return f'URL -> {self.url}\n' \
               f'RUTA -> {self.ruta}\n' \
               f'FORMATO -> {self.formato}\n' \
               f'CONTENIDO -> {self.contenido}\n' \
               f'TITULO -> {self.titulo}\n' \
               f'SLUG -> {self.slugificar(self.titulo)}\n' \
               f'META-TAGS -> {self.meta_tagas}'

