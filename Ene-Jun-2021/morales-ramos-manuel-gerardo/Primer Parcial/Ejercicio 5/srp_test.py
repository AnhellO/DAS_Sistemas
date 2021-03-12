import unittest

from srp import *

class Srp(unittest.TestCase):
    def test_to_str(self):
        usuario = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )

        result = Serializar(usuario).to_str()

        self.assertEqual('Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z',result)

    def test_to_json(self):
        usuario = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )

        result = Serializar(usuario).to_json()

        self.assertEqual('{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}',result)

if __name__ == "__main__":
    unittest.main()