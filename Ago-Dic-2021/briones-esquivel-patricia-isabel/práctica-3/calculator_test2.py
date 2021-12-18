from calculator import *

def test_calc_suma():
   assert Calculator(5,10).suma() == 15

def test_calc_resta():
   assert Calculator(19,8).resta() == 11

def test_calc_multiplicacion():
   assert Calculator(3,5).multiplicacion() == 15

def test_calc_division():
   test_cases = [
      (8, 4, 2), #Test case: División simple
      (3, 0, 'error'), #Test case: División entre 0
      ]

   for tc in test_cases:
      assert Calculator(tc[0],tc[1]).division() == tc[2]

def test_calc_potencia():
   # [0] Número a potenciar, [1] Potencia, [2] resultado
   test_cases = [
      (5, 2, 25), #Test case: Potencia simple
      (5, -2, 0.04), #Test case: Potencia negativa
      ]

   for tc in test_cases:
      assert Calculator(tc[0],tc[1]).potencia() == tc[2]

def test_calc_raiz():
   # [0] Número a sacar raíz, [1] índice de raíz, [2] resultado
   test_cases = [
      (25, 2, 5), #Test case: Raiz simple
      (-1, 2, 'error'), #Test case: Raíz de un número negativo
      ]

   for tc in test_cases:
      assert Calculator(tc[0],tc[1]).raiz() == tc[2]
