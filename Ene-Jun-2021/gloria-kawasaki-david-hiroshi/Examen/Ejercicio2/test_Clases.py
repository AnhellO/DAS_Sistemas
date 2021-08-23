import unittest
from Clases import PaginaWeb as pagWeb
from Clases import SitioWeb as SitWeb

'''
Casos de prueba de la clase Clases
'''
class TestClases(unittest.TestCase):
    def test_Just_One_Page(self):
        self.url="www.facebook.com/Hiroshi"
        self.ruta="/facebook/Usuarios/Hiroshi"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Hiroshi en Facebook</p></body>"
        self.titulo="Facebook de Hiroshi"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')
        self.pagina = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)
        self.mettags = ",".join(self.metatags)
        self.r=f'URL: {self.url}'
        self.r+=f'\nRUTA: {self.ruta}'
        self.r+=f'\nFORMATO: {self.formato}'
        self.r+=f'\nCONTENIDO: {self.contenido}'
        self.r+=f'\nTITULO: {self.titulo}'
        self.r+=f'\nSLUG: {self.slug}'
        self.r+=f'\nMETA-TAGS: {self.mettags}'
        self.assertEqual(str(self.pagina),self.r)

    '''
    Para este caso de prueba, solo se agregó 4 veces la misma página para poblar la lista
    '''
    def test_Just_One_SiteWeb_With_4_Pages(self):
        self.url="www.facebook.com/Hiroshi"
        self.ruta="/facebook/Usuarios/Hiroshi"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Hiroshi en Facebook</p></body>"
        self.titulo="Facebook de Hiroshi"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')

        self.pagina1 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)
        self.pagina2 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)
        self.pagina3 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)
        self.pagina4 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)

        self.dominio="facebook.com"
        self.categoria="red social"
        self.paginas=[]
        self.paginas.append(self.pagina1)
        self.paginas.append(self.pagina2)
        self.paginas.append(self.pagina3)
        self.paginas.append(self.pagina4)
        self.sitio = SitWeb(self.dominio,self.categoria,self.paginas)
        
        self.r=f"DOMINIO: {self.dominio}"
        self.r+=f"\nCATEGORIA: {self.categoria}"
        self.r+=f"\nPAGINAS:\n"
        self.r+="############\n"
        self.r+=f"{self.pagina1}\n"
        self.r+="############\n"
        self.r+=f"{self.pagina2}\n"
        self.r+="############\n"
        self.r+=f"{self.pagina3}\n"
        self.r+="############\n"
        self.r+=f"{self.pagina4}\n"
        self.assertEqual(str(self.sitio),self.r)

    '''
    Para este caso, se tuvo que poblar la lista con diferentes páginas para probar el buscador
    '''
    def test_Buscador(self):
        self.url="www.facebook.com/Hiroshi"
        self.ruta="/facebook/Usuarios/Hiroshi"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Hiroshi en Facebook</p></body>"
        self.titulo="Facebook de Hiroshi"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')
        self.pagina1 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)

        self.url="www.facebook.com/Yareeny"
        self.ruta="/facebook/Usuarios/Yareeny"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Yareeny en Facebook</p></body>"
        self.titulo="Facebook de Yareeny"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')
        self.pagina2 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)

        self.url="www.facebook.com/Mario"
        self.ruta="/facebook/Usuarios/Mario"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Mario en Facebook</p></body>"
        self.titulo="Facebook de Mario"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')
        self.pagina3 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)

        self.url="www.facebook.com/Angela"
        self.ruta="/facebook/Usuarios/Angela"
        self.formato="HTML"
        self.contenido="<head></head><body><p>Hola, soy Angela en Facebook</p></body>"
        self.titulo="Facebook de Angela"
        self.slug=((self.titulo).lower()).replace(" ","-")
        self.metatags = ('asdf','qwer','zxcv','tyui')
        self.pagina4 = pagWeb(self.url,self.ruta,self.formato,self.contenido,self.titulo,self.slug,self.metatags)

        self.paginas=[]
        self.paginas.append(self.pagina1)
        self.paginas.append(self.pagina2)
        self.paginas.append(self.pagina3)
        self.paginas.append(self.pagina4)
        self.dominio="facebook.com"
        self.categoria="red social"
        self.sitio = SitWeb(self.dominio,self.categoria,self.paginas)
        self.buscador = self.sitio.buscador(self.pagina1)
        self.assertEqual(self.buscador,"Existe.")

if __name__ == '__main__':
    unittest.main()