from random import randint
class Die():
    def __init__(self,lados) :
        self.lados=lados
    def roll_die(self):
        print (randint(1,int(self.lados)))

print ("dado de 6 caras")
dado_6=Die(6)
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()
dado_6.roll_die()

print ("\ndado de 10 caras")
dado_10=Die(10)
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()
dado_10.roll_die()

print ("\ndado de 20 caras")
dado_20=Die(20)
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()
dado_20.roll_die()


