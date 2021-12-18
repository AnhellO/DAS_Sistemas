class Die():
    
    def __init__(self):
        self.sides = 6
    
    def Change_Sides(self, sides):
        self.sides = sides
    
    def Roll(self):
        print(randint(1,self.sides))

D6 = Die()
print("\nD6:")
for i in range(10):
    D6.Roll()
    
D10 = Die()
D10.Change_Sides(10)
print("\nD10:")
for i in range(10):
    D10.Roll()
    
D20 = Die()
D20.Change_Sides(20)
print("\nD20:")
for i in range(10):
    D20.Roll()