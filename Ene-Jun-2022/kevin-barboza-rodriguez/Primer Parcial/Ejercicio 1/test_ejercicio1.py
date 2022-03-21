import unittest
from ejercicio_1 import *

class PageTest(unittest.TestCase):

    def test_crear_objetos(self):
        pagina = Page(html="<html>", head="<head>", link="<link>", title="<title>",
                      body="<body>", h1="<h1>", p="<p>", div="<div>", json="<script>")
        self.assertIsInstance(pagina, Page)

        sitio_web = Website("kevin code", subdominio="html",
                            url="www.kevincode.com", contacto="kevin@gmail.com")
        self.assertIsInstance(sitio_web, Website)

    def test_buscador(self):
        pagina = Page(html="<html>", head="<head>", link="<link>", title="<title>",
                      body="<body>", h1="<h1>", p="<p>", div="<div>", json="<script>")
        sitio_web = Website("kevin code", subdominio="html",
                        url="www.kevincode.com", contacto="kevin@gmail.com")
        sitio_web.coleccion.append(pagina)

        busqueda = buscador(sitio_web, pagina)
        self.assertEqual(busqueda, "this page is on this website")

if __name__ == "__main__":
    unittest.main()
