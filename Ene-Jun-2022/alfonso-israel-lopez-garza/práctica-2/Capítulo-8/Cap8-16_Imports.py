import Sandwich 
from Sandwich import sandwich
from Sandwich import sandwich as sn
import Sandwich as Sand
from Sandwich import *


##Usando modulo completo
Sandwich.sandwich('carne','lechuga','jamon','aguacate') 
Sand.sandwich('lechuga', 'jamon','mayonesa') 

#Usando la función del modulo
sandwich('huevo','aguacate','mayonesa','lechuga')
sn('jamon','huevo')

