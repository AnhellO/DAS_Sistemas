# Pruebas PyTest#
from calculator import *

def test_suma():
   assert Calculator(5,10).suma() == 15

def test_resta():
   assert Calculator(19,8).resta() == 11

def test_multiplicacion():
   assert Calculator(5,9).multiplicacion() == 45

def test_calc_division():
   test_cases = [
      (25, 5, 5),
      #División entre 0#
      (6, 0, "Math ERROR"), 
      ]

   for tc in test_cases:
      assert Calculator(tc[0],tc[1]).division() == tc[2]

def test_potencia():
   assert Calculator(2,4).potencia() == 16

def test_raiz():
   test_cases = [
      (8, 3, 2), 
      #Raíz de un número negativo#
      (-1, 2, 'Math ERROR'),
      ]
   for tc in test_cases:
      assert Calculator(tc[0],tc[1]).raiz() == tc[2]