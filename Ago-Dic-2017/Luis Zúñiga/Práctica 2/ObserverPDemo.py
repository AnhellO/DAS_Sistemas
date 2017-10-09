import time
import random
from Observer import Observer
import os
from Subject import Subject
from BinaryObserver import BinaryObserver
from OctalObserver import OctalObserver
from HexObserver import HexObserver

sujeto = Subject

observador = Observer(sujeto)
observador = BinaryObserver(sujeto)
observador = OctalObserver(sujeto)
observador = HexObserver(sujeto)

for x in range(20, 0, -1):
    os.system('cls')
    r = random.randint(0,1000)
    sujeto.setState(sujeto,r)    
    time.sleep(2)



