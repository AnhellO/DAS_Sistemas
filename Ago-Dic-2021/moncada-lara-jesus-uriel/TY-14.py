"""Try it yourself 9-13 """

from random import randint

class Dice():
    def __init__(self,faces=6):
        self.faces = faces
    
    def roll_die(self):
        print( randint(1, self.faces))
print("primeras 10 tiradas con un dado de 6 caras \n")
tirada = Dice()

for i in range(10):
    tirada.roll_die()

print("\n Siguientes 10 tiradas con un dado de 10 caras \n")
tirada = Dice(faces=10)
for i in range(10):
    tirada.roll_die()

print("\n Siguientes 10 tiradas con un dado de 20 caras \n")
tirada = Dice(faces=20)
for i in range(10):
    tirada.roll_die()
