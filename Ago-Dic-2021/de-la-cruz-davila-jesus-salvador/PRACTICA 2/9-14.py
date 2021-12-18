from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        return randint(1, self.sides)
    
    
side = Die()


results = []

for roll_num in range(10):
    result = side.roll_die()
    results.append(result)

print("Dado de 6 caras lanzado 10 veces")
print(results)
print("")


# Para un dado de 10 caras

side10 = Die(sides = 10)

results = []

for roll_num in range(10):
    result = side10.roll_die()
    results.append(result)

print("Dado de 10 caras lanzado 10 veces")
print(results)
print("")


# Para un dado de 20 caras

side20 = Die(sides = 20)

results = []

for roll_num in range(10):
    result = side20.roll_die()
    results.append(result)
    

print("Dado de 20 caras lanzado 10 veces")
print(results)


