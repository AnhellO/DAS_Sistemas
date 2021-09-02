import unittest
from factory import *

class Test_Factory(unittest.TestCase):
    def test_instancia(self):
        escaleno = ConcreteProductEscaleno(90,60,30,10,20,30)
        factory = ConcreteCreatorEscaleno().get_triangulo(escaleno)
        self.assertIsInstance(factory, ConcreteProductEscaleno)
    
    def test_Equilatero(self):
        equilatero = ConcreteProductEquilatero(90,60,30,20,20,20)
        self.assertEqual(equilatero.verificar_triangulo(), True)
    
    def test_Isoceles(self):
        isoceles = ConcreteProductIsoceles(90,60,30,10,10,20)
        self.assertEqual(isoceles.verificar_triangulo(), True)
    
    def test_Escaleno(self):
        escaleno = ConcreteProductEscaleno(90,60,30,15,25,35)
        self.assertEqual(escaleno.verificar_triangulo(), True)
    
    def test_Equilatero_False(self):
        equilatero = ConcreteProductEquilatero(90,60,30,10,20,20)
        self.assertEqual(equilatero.verificar_triangulo(), False)
    
    def test_Isoceles_False(self):
        isoceles = ConcreteProductIsoceles(90,60,30,10,10,10)
        self.assertEqual(isoceles.verificar_triangulo(), False)
    
    def test_Escaleno_False(self):
        escaleno = ConcreteProductEscaleno(90,60,30,10,10,20)
        self.assertEqual(escaleno.verificar_triangulo(), False)

if __name__ == "__main__":
    unittest.main()