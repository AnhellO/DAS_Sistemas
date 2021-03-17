import unittest

from srp import *

class SingleResponsibilityPrincipleTest(unittest.TestCase):
    def test_user_creation(self):
        user = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )
        
        self.assertEqual(user.get_nombre(), 'Ramanujan')
        self.assertEqual(user.get_edad(), 25)
        self.assertEqual(user.get_direccion(), 'Calle X, #Y Colonia Z')
    
    def test_user_modification(self):
        user = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )
        
        # Test antes y después de hacer 'set'
        self.assertEqual(user.get_nombre(), 'Ramanujan')
        user.set_nombre('Gauss')
        self.assertEqual(user.get_nombre(), 'Gauss')
        
        self.assertEqual(user.get_edad(), 25)
        user.set_edad(28)
        self.assertEqual(user.get_edad(), 28)
        
        self.assertEqual(user.get_direccion(), 'Calle X, #Y Colonia Z')
        user.set_direccion('aasdfg')
        self.assertEqual(user.get_direccion(), 'aasdfg')
    
    def test_to_string(self):
        user = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )
        
        self.assertEqual(str(user), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z')
    
    def test_serialize_to_string(self):
        user = Usuario(
            nombre='X',
            edad=25,
            direccion='Y'
        )
        
        serializer = Serializador(user)
        self.assertEqual(serializer.serializar(), 'Nombre: X\nEdad: 25\nDireccion: Y')
    
    def test_serialize_to_dict(self):
        user = Usuario(
            nombre='X',
            edad=25,
            direccion='Y'
        )
        
        serializer = Serializador(user)
        self.assertEqual(serializer.serializar('diccionario'), {'nombre': 'X', 'edad': 25, 'direccion': 'Y'})
    
    def test_serialize_to_json(self):
        user = Usuario(
            nombre='X',
            edad=25,
            direccion='Y'
        )
        
        serializer = Serializador(user)
        self.assertEqual(serializer.serializar('json'), '{"nombre": "X", "edad": 25, "direccion": "Y"}')
    
    def test_serialize_to_html(self):
        user = Usuario(
            nombre='X',
            edad=25,
            direccion='Y'
        )
        
        serializer = Serializador(user)
        self.assertEqual(serializer.serializar('html'), '<table border="1"><tr><th>nombre</th><td>X</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Y</td></tr></table>')


if __name__ == "__main__":
    unittest.main()