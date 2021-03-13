import json
import unittest
from srp import Usuario

class Test_srp(unittest.TestCase):
    def test_serializarString(self):
        user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        retorno = "Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z"
        self.assertEqual(user.serializarString(),retorno)
    def test_serializarStr(self):
        user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        retorno = {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}
        self.assertEqual(user.serializarDict(),retorno)
    def test_serializarJson(self):
        user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        retorno = {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}
        retorno = json.dumps(retorno)
        self.assertIn(user.serializarJson(),retorno)
    def test_serializarHtml(self):
        user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        retorno = '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>'
        self.assertEqual(user.serializarHtml(),retorno)

if __name__=='__main__':
    unittest.main()