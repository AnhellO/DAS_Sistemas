import sys
sys.path.append('../')
import unittest
import mock
from mock import patch

from Especial.Ejercicio4.srp import *

#********************************************************************************************************
#*          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PRUEAS UNITARIAS  <<<<<<<<<<<<<<<<<<<<<<              *
#********************************************************************************************************

class srptest(unittest.TestCase):
    def test_serialize(self):
        mock = ["formato='string'"]
        self.assertEqual('Nombre:juanito, Edad:15, direccion:calle x, #y colonia z')

    def test_Usuario(self):
        class Mock_User:
            def __init__(self, nombre, edad, direccion):
                self.nombre = nombre
                self.edad = edad
                self.direccion = direccion
        mock_nombre='Nombre:juanito'
        user=serializar
        self.assertEqual('Nombre:juanito', mock_nombre)