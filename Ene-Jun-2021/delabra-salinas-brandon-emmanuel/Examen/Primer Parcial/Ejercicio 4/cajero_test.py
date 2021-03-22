import unittest
from cajero import CajeroATMChain

class Test_cajero(unittest.TestCase):
   
    def Test_ATM(self):
        resultado = CajeroATMChain(5)
        self.assertEqua(resultado, "debes dar una cantidad multiplo de 10 ")

       
    def Test_ATM2(self):
        resultado = CajeroATMChain(10)
        self.assertEqua(resultado, "Dar 1 $10 ")

    def Test_ATM3(self):
        resultado = CajeroATMChain(50)
        self.assertEqua(resultado, "Dar 1 $50 ")

if __name__ == "__main__":
     unittest.main()
    
