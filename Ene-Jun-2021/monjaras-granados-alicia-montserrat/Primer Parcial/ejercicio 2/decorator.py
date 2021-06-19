import abc

class PaginaWeb:# Es un documento que se puede mostrar en un navegador web

    def __init__(self, url, ruta, formato, contenido, titulo, slug, meta_tags):# # constructor 
        # declara atributos
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido =  contenido
        self.titulo = titulo
        self.slug = slug
        self.meta_tags = meta_tags
      
    def __str__(self) -> str: # imprime de forma legible el objeto

        return f"Url: {self.url}\nRuta: {self.ruta}\nFormato: {self.formato}\nContenido: {self.contenido}\nTítulo: {self.titulo}\nSlug: {self.slug}\nMeta-tags: {' '.join([str(i) for i in self.meta_tags])}"


# Interface
class Component(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def buscador(self) -> str:
        pass

# Clase Decorator
class Decorator(Component):

    _wrapper: Component = None

    def __init__(self, component: Component) :
        self._wrapper = component

    c = _wrapper

    def BaseDecorator(self, c: Component) -> str:
        return self._wrapper

    def buscador(self) -> str:
        return self._wrapper.buscador()
        
# Concrete Component
class BuscadorConcreteDecorator(Decorator):

   def buscador(self, pagina:PaginaWeb) -> str:
        if pagina in self._wrapper.buscador():
            return "La página existe"
        else:
            return "No existe la página"
    

class SitioWeb(Component):

    def __init__(self, dominio, categoria, paginas:PaginaWeb):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas

    def buscador(self) :
        return self.paginas
    
    def __str__(self) -> str :

        return f"Dominio: {self.dominio}\nCategoria: {self.categoria}\nPaginas: {len(self.paginas)}\n {''.join([str(i) for i in self.paginas])}"



def main():
    pagina_1 = PaginaWeb( 
        url =  "https://instaprint.es/",  
        ruta =  "/epages/",
        formato = "HTML", 
        contenido = '<a href= "https://instaprint.es/epages/342de146-c59c-467f-1664/Categories/Contactanos/Nuestras_Tiendas">"Visita Nuestros Nuevos centros de impresión y recojidas en Barcelona y alrededores."</a>', 
        titulo = '<h1 style="vertical-align: inherit;">Instaprint: Imprenta Online 24 hrs</h1>', 
        slug = "instaprint-imprenta-online-24-hrs", 
        meta_tags= ['<meta name="Nombre del elemento" content="Contenido asignado"/>','<meta charset="utf-8"/>', '<meta name="robots" content="index"/>'])
    #print(pagina_1)

    pagina_2 = PaginaWeb( 
        url =  "https://saviabruta.com/",  
        ruta =  "/root/", 
        formato = "HTML", 
        contenido =  '<p>Crear un estudio de diseño floral en Madrid dedicado a la creación de composiciones florales hechos con cariño y atención al detalle.</p>', 
        titulo = '<h1 class="elementor-heading-title elementor-size-default">Floristería<br>en Madrid</h1>', 
        slug = "florerista-en-madrid", 
        meta_tags= ['<meta name="robots" content="max-image-preview:large">','<meta charset="utf-8"/>','<meta property="og:type" content="website">'])
    #print(pagina_2)

    pagina_3 = PaginaWeb( 
        url =  "https://ejemplo.com/",  
        ruta =  "/root/", 
        formato = "HTML", 
        contenido =  '<p>Crear un estudio de diseño floral en Madrid dedicado a la creación de composiciones florales hechos con cariño y atención al detalle.</p>', 
        titulo = '<h1 class="elementor-heading-title elementor-size-default">Floristería<br>en Madrid</h1>', 
        slug = "florerista-en-madrid", 
        meta_tags= ['<meta name="robots" content="max-image-preview:large">','<meta charset="utf-8"/>','<meta property="og:type" content="website">'])
    

    sitio_web = SitioWeb(
        dominio= 'https://admin.dominiomuestra.com',
        categoria= 'Comerciales',
        paginas= [pagina_1,pagina_2]
    )

    print(sitio_web)
    buscar = BuscadorConcreteDecorator(sitio_web)
    resultado = buscar.buscador(pagina_3)
    print(resultado)
        

if __name__ == "__main__":
     main()