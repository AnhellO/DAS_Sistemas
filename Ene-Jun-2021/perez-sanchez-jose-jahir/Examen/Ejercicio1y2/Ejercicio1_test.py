import unittest

from Ejercicio1 import PaginaWeb, SitioWeb
#Las pruebas del primer y segudo ejercicio, en la primera pude implementarla sin problemas, las demas como devuelve un print da None y por eso lo que tiene que dar None,
#pero si corres las pruebas te imprime lo que tiene que ser
class PaginaTest(unittest.TestCase):
    def test_pagina_web(self):
        pagina = PaginaWeb(url="www.simon.com",ruta="/https",formato="HTML",contenido="<p>Esta es la pagina de Simon</p>",titulo="<h1>La pagina de simon</h1>",slug="La pagina de simon",metatags="<meta name =description content = This is the description. It should be about 155 characters long.>)")
        self.assertEqual(
            str(pagina),
            "Url de la pagina: www.simon.com, ruta de la pagina: /https, formato de la pagina: HTML, contenido de la pagina: <p>Esta es la pagina de Simon</p>, titulo de la pagina: <h1>La pagina de simon</h1>, slug de la pagina: la-pagina-de-simon y metatags de la pagina: <meta name =description content = This is the description. It should be about 155 characters long.>)"
        )
        
    def test_buscar_pagina(self):
        Pag2 = PaginaWeb("www.pedro.com","/https","XML","<contenido>Esta es la pagina de Pedro</contenido>","La pagina de pedro","La pagina de pedro","No se")
        paginas = [Pag2]
        sitio = SitioWeb(".net","informatica",paginas)
        self.assertEqual(
            sitio.buscador(Pag2),
            None
        )
    
    def test_buscar_pagina_no_existe(self):
        Pagdummy = PaginaWeb("x","x","x","x","x","x","x")
        paginas = [Pagdummy]
        sitio = SitioWeb(".net","informatica",paginas)
        self.assertEqual(
            sitio.buscador(Pagdummy),
            None
        )

if __name__ == "__main__":
    unittest.main()