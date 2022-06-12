from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    
    def roll_die(self):
        '''Imprime un numero random entre 1 y el numero de sides'''
        print(randint(1,self.sides), end=", ")
    
#instancia

girar = Die()

for i in range(girar.sides):
    for j in range(10):
        girar.roll_die()
    print()
