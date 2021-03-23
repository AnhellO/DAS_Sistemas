'''
class CharacterConcreteComponent(object):
    def __init__(self, name: str): #Damos como parámetro una función
        print ("Luxor equipment:")
        self.name = name #La almacenamos en el constructor  
    def equip(self):
        return f"{self._name} equipment:"

    def __call__(self): #La definimos como llamable
        self.name() #Ejecutamos la funcion en call
'''
def CharacterConcreteComponent(name: str): #Creamos la función decorador (A) con el argumento func
    def BaseDecorator(): #Creamos la nueva función (C)  
        print ("Luxor equipment:")#Añadimos una modificación a la función (B) dentro de (C)
        name() #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A)
    return BaseDecorator #Para devolver (C)

@CharacterConcreteComponent
# Concrete Decorator Armor
def ArmorConcreteDecorator():
    print("Armor: Yes")
ArmorConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator Sword
def SwordConcreteDecorator():
    print("Sword: Yes")
SwordConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator Sword And Armor
def SwordandArmorConcreteDecorator():
    print("Armor: Yes\nSword: Yes")
SwordandArmorConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator Ring
def RingConcreteDecorator():
    print("Ring: Yes")
RingConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator Shield
def ShieldConcreteDecorator():
    print("Shield: Yes")
ShieldConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator Ring And Shied
def RingAndShieldConcreteDecorator():
    print("Ring: Yes\nShield: Yes")
RingAndShieldConcreteDecorator()

@CharacterConcreteComponent
# Concrete Decorator All
def AllConcreteDecorator():
     print("Armor: Yes\nSword: Yes\nRing: Yes\nShield: Yes")
AllConcreteDecorator()