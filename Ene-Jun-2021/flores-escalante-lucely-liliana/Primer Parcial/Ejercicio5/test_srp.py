import unittest

import json

from srp import *

class Test_srp(unittest.TestCase):

    def test_serializarString(self):
        usuario = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')

        self.assertEqual(usuario.serializarString(),"Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z")

    def test_serializarDiccionario(self):
        usuario = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')

        self.assertEqual(usuario.serializarJson(),{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"})

    def test_serializarJson(self):
        usuario = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        resultado = {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}
        resultado = json.dumps(resultado)

        self.assertIn(usuario.serializarJson(),json.dumps({"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}))

    def test_serializarHtml(self):
        usuario = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')

        self.assertEqual(usuario.serializarHtml(),'<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')

if __name__=='__main__':
    unittest.main()