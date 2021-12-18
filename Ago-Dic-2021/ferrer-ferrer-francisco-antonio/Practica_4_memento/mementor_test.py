import unittest

from Originador import *

class Mementor_test(unittest.TestCase):


    def test_detalles_Celular(self):
        cel = Celular('Samsung','Galaxy','A10s')
        self.assertEqual(('Samsung','Galaxy','A10s'), cel.get_detalles_celular())

    def test_get_state_memento(self):
        cel = Memento('Samsung','Galaxy','A10s')
        self.assertEqual(('Samsung','Galaxy','A10s'), cel.get_state()) 
    
    def test_agregar_algo_cuidador(self):#doSomething
        
        almacen = Cuidador()
        cell = Celular('Samsung','Galaxy','A10s')
        almacen.doSomething(cell.save())
        self.assertEqual(('Samsung','Galaxy','A10s'), cell.get_detalles_celular())

    # def test_restaurar_celular(self):

    #     almacen = Cuidador()
    #     cell = Celular('','','')
    #     cell.agregar_celular('Samsung','Galaxy','A10s')
        
    #     almacen.doSomething(cell.save())
    #     cell.agregar_celular('Samsung','SGH','X48')
    #     self.assertEqual(('Samsung','SGH','X48'), cell.get_detalles_celular())

    #     cell.restore(almacen.undo())
    #     self.assertEqual(('Samsung','Galaxy','A10s'), cell.get_detalles_celular())



if __name__ == "__main__":
    unittest.main()
  
    #py -m pytest Practica_4_memento/mementor_test.py