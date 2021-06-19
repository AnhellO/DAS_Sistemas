import unittest

from srp import *
#Las pruebas unitarias que realize mientras refactorizaba
class SrpTest(unittest.TestCase):
    def test_string(self):
        user = Usuario(
                nombre='Ramanujan',
                edad=25,
                direccion='Calle X, #Y Colonia Z'
        )
        self.assertEqual(user.serializar("string"),"Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z")

    def test_dic(self):
        user = Usuario(
                nombre='Ramanujan',
                edad=25,
                direccion='Calle X, #Y Colonia Z'
        )
        self.assertEqual(user.serializar("diccionario"),{'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'})

    def test_json(self):
        user = Usuario(
                nombre='Ramanujan',
                edad=25,
                direccion='Calle X, #Y Colonia Z'
        )
        self.assertEqual(user.serializar("json"),'{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}')

    def test_html(self):
        user = Usuario(
                nombre='Ramanujan',
                edad=25,
                direccion='Calle X, #Y Colonia Z'
        )
        self.assertEqual(user.serializar("html"), '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')

if __name__ == "__main__":
    unittest.main()