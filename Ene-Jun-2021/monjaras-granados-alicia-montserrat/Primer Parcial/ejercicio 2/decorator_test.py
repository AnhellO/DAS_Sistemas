import unittest

from decorator import *

class DecoratorTest(unittest.TestCase):
    def test_pagina_exitoso(self):
        pagina_1 = PaginaWeb( 
            url =  "https://instaprint.es/",  
            ruta =  "/epages/",
            formato = "HTML", 
            contenido = '<a href= "https://instaprint.es/epages/342de146-c59c-467f-1664/Categories/Contactanos/Nuestras_Tiendas">"Visita Nuestros Nuevos centros de impresión y recojidas en Barcelona y alrededores."</a>', 
            titulo = '<h1 style="vertical-align: inherit;">Instaprint: Imprenta Online 24 hrs</h1>', 
            slug = "instaprint-imprenta-online-24-hrs", 
            meta_tags= ['<meta name="Nombre del elemento" content="Contenido asignado"/>','<meta charset="utf-8"/>', '<meta name="robots" content="index"/>'])
        
        sitio_web = SitioWeb(
            dominio= 'https://admin.dominiomuestra.com',
            categoria= 'Comerciales',
            paginas= [pagina_1]
        )
        pagina_buscar=BuscadorConcreteDecorator(sitio_web)
        self.assertEqual(pagina_buscar.buscador(pagina_1),"La página existe")

    def test_pagina_pagina_no_encontrada(self):
        pagina_1 = PaginaWeb( 
            url =  "https://instaprint.es/",  
            ruta =  "/epages/",
            formato = "HTML", 
            contenido = '<a href= "https://instaprint.es/epages/342de146-c59c-467f-1664/Categories/Contactanos/Nuestras_Tiendas">"Visita Nuestros Nuevos centros de impresión y recojidas en Barcelona y alrededores."</a>', 
            titulo = '<h1 style="vertical-align: inherit;">Instaprint: Imprenta Online 24 hrs</h1>', 
            slug = "instaprint-imprenta-online-24-hrs", 
            meta_tags= ['<meta name="Nombre del elemento" content="Contenido asignado"/>','<meta charset="utf-8"/>', '<meta name="robots" content="index"/>'])
        
        
        pagina_2 = PaginaWeb( 
            url =  "https://saviabruta.com/",  
            ruta =  "/root/", 
            formato = "HTML", 
            contenido =  '<p>Crear un estudio de diseño floral en Madrid dedicado a la creación de composiciones florales hechos con cariño y atención al detalle.</p>', 
            titulo = '<h1 class="elementor-heading-title elementor-size-default">Floristería<br>en Madrid</h1>', 
            slug = "florerista-en-madrid", 
            meta_tags= ['<meta name="robots" content="max-image-preview:large">','<meta charset="utf-8"/>','<meta property="og:type" content="website">'])
        
        sitio_web = SitioWeb(
            dominio= 'https://admin.dominiomuestra.com',
            categoria= 'Comerciales',
            paginas= [pagina_1]
        )
        pagina_buscar=BuscadorConcreteDecorator(sitio_web)
        self.assertEqual(pagina_buscar.buscador(pagina_2),"No existe la página")


if __name__=="__main__":
    unittest.main()