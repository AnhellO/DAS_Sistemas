import unittest
from ejercicio_2 import *


class DirectorTest(unittest.TestCase):

    def test_crear_objetos(self):
        web_site = ConcreteWebsite("kevin code",subdominio="html",url="www.kevincode.com",contacto="kevin@gmail.com")
        self.assertIsInstance(web_site, ConcreteWebsite)

        page = ConcretPage(html="<html>", head="<head>", link="<link>", title="<title>",
                  body="<body>", h1="<h1>", p="<p>", div="<div>", json="<script>")
        self.assertIsInstance(page, ConcretPage)


if __name__ == "__main__":
    unittest.main()
