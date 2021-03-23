import unittest
from srp import Usuario

class Test_srp(unittest.TestCase):
    def test_serializarString(self):
        u = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        resultado = "Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z"
        self.assertEqual(u.serializarString(),resultado)

    def test_serializarStr(self):
        u = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        resultado = {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}
        self.assertEqual(u.serializarDict(),resultado)
    def test_serializarJson(self):
        u = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        resultado = {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}
        resultado = json.dumps(resultado)
        self.assertIn(u.serializarJson(),resultado)
    def test_serializarHtml(self):
        u = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z')
        resultado = '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>'
        self.assertEqual(u.serializarHtml(),resultado)