import json
import unittest
from srp import Usuario

class Test_srp(unittest.TestCase):


    def test_serializarStr(self):
        user = Usuario(nombre='Freddy Krueger', edad=40, direccion='Elm Street')
        resultado = {"nombre": "Freddy Krueger", "edad": 40, "direccion": "Elm Street"}#agaregamos un diccionario para la prueba 
        self.assertEqual(user.serializarDict(),resultado)

    def test_serializarJson(self):
        user = Usuario(nombre='Freddy Krueger', edad=40, direccion='Elm Street')
        resultado = {"nombre": "Freddy Krueger", "edad": 40, "direccion": "Elm Street"}
        resultado = json.dumps(resultado)
        self.assertIn(user.serializarJson(),resultado)

    def test_serializarString(self):
        user = Usuario(nombre='Freddy Krueger', edad = 40, direccion = 'Elm Street')
        resultado = "Nombre: Freddy Krueger\nEdad: 40\nDireccion: Elm Street"
        self.assertEqual(user.serializarString(),resultado)


if __name__=='__main__':
    unittest.main()