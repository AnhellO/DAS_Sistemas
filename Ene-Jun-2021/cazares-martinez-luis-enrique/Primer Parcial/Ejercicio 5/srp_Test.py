import unittest
from srp import Usuario

#Se crea la suite unitaria de acuerdo al RGF
class RGFTest(unittest.TestCase):

    # Red Test: Se crea una prueba unitaria la cual debe fallar.
    
    # def test_RS(self):
    #     user = Usuario(
    #         nombre='Ramanujan',
    #         edad=25,
    #         direccion='Calle X, #Y Colonia Z'
    #     )
    #
    #     test_cases = [
    #         (user.serializarString(), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'),
    #         (user.serializarDiccionario(), {'nombre': 'Ramanujan', 'edad': 25, 'direccion': 'Calle X, #Y Colonia Z'}),
    #         (user.serializarJSON(), {"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}),
    #         (user.serializarHTML(), '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')]
    #
    #     for entrada, esperado in test_cases:
    #         actual = entrada
    #         self.assertEqual(esperado, actual)
    

    # Green Test: Se crea una prueba unitaria la cual corrige el "Red test" no debe fallar
    
    # def test_GS(self):
    #     user = Usuario(
    #         nombre='Ramanujan',
    #         edad=25,
    #         direccion='Calle X, #Y Colonia Z'
    #     )
    #
    #     test_cases = [
    #         (user.serializarString(), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'),
    #         (user.serializarDiccionario(), {'direccion': 'Calle X, #Y Colonia Z', 'edad': 25, 'nombre': 'Ramanujan'}),
    #         (user.serializarJSON(), '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}'),
    #         (user.serializarHTML(), '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')]
    #
    #     for entrada, esperado in test_cases:
    #         actual = entrada
    #         self.assertEqual(esperado, actual)


    # Refactoring
    def test_RS(self):
        user = Usuario(
            nombre='Ramanujan',
            edad=25,
            direccion='Calle X, #Y Colonia Z'
        )

        test_cases = [
            (user.serializarString(), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'),
            (user.serializarDiccionario(), {'direccion': 'Calle X, #Y Colonia Z', 'edad': 25, 'nombre': 'Ramanujan'}),
            (user.serializarJSON(), '{"nombre": "Ramanujan", "edad": 25, "direccion": "Calle X, #Y Colonia Z"}'),
            (user.serializarHTML(),
             '<table border="1"><tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr></table>')]

        for entrada, esperado in test_cases:
            self.assertEqual(esperado, entrada)


if __name__ == '__main__':
    unittest.main()
