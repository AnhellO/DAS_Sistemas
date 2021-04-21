#Goncho
import unittest
from srp import Usuario

class RGFTest(unittest.TestCase):
    #Se fue implementando el Red - Green Refactoring Paso a paso como vimos en clase en la siguiente funcion empezamos con el 'Red - Green Refactoring = *RED*
    # Red Test
    #despues se fue implementando el Red - Green Refactoring Paso a paso como vimos en clase en la siguiente funcion empezamos con el 'Red - Green Refactoring = *GREEN*
    # Green Test
    def Green_Test(self):
         user = Usuario(
             nombre='Ramanujan',
             edad=25,
             direccion='Calle X, #Y Colonia Z'
         )
    
         test_cases = [
             (user.serializarString(), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'),
             (user.serializarDiccionario(), {'nombre': 'Gonzalo', 'edad': 26, 'direccion': 'Calle X, #Y Colonia Z'}),
             (user.serializarJSON(), {"nombre": "Eduardo", "edad": 99, "direccion": "Calle X, #Y Colonia Z"}),
             (user.serializarHTML(), '<tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr>')]
    
         for entrada, esperado in test_cases:
             actual = entrada
             self.assertEqual(esperado, actual)

    #Y al funal se fue implementando el Red - Green Refactoring Paso a paso como vimos en clase en la siguiente funcion empezamos con el 'Red - Green Refactoring = *REFACTORING*
    # Refactoring
    def Refactoring_Test(self):
        user = Usuario(
            nombre='Gonzalo',
            edad=26,
            direccion='Calle X, #Y Colonia Z'
        )
        test_cases = [
             (user.serializarString(), 'Nombre: Ramanujan\nEdad: 25\nDireccion: Calle X, #Y Colonia Z'),
             (user.serializarDiccionario(), {'nombre': 'Gonzalo', 'edad': 26, 'direccion': 'Calle X, #Y Colonia Z'}),
             (user.serializarJSON(), {"nombre": "Eduardo", "edad": 99, "direccion": "Calle X, #Y Colonia Z"}),
             (user.serializarHTML(), '<tr><th>nombre</th><td>Ramanujan</td></tr><tr><th>edad</th><td>25</td></tr><tr><th>direccion</th><td>Calle X, #Y Colonia Z</td></tr>')]
    
        for entrada, esperado in test_cases:
            self.assertEqual(esperado, entrada)


if __name__ == '__main__':
    unittest.main()

#Este ejercicio lo hice siguiendo el enfoque  'Red - Green Refactoring' a como le entendi realmente no se si es como realmente deberia de ser pero pues este fue el resultado al final jalo y ya no quice moverle mas jaja :V

"""
¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
    RESPUESTA = solo implementar una nueva funcion para la nueva serializacion que se van a implementar



¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
    RESPUESTA = Creo que podria ser crear una clase que especifica para serializacion y que resiva como atributo un objeto

"""