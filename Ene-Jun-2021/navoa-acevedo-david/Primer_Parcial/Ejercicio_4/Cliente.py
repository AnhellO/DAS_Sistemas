import sys
from CajeroATMChain import CajeroATM

ATM = CajeroATM()
Cantidad = int(input("Inserte la cantidad a retirar : "))
if Cantidad < 10 or Cantidad % 10 != 0:
    print("La cantidad a retirar debe ser mayor a 10 y en multiplos de 10.")
    sys.exit()

ATM.chain1.handle(Cantidad)