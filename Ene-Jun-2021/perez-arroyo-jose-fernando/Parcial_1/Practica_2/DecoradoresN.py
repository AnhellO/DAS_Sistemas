class componente:
    def equip(self):
        pass

class CharacterConcreteComponent(componente):
    def __init__(self, name: str):
        self.name = name 
        self.p1 = ''

    def e2(x):
        def a2(self):
           return f"{self.name} equipment:"+ x(self)
        return a2
    @e2
    def equip(self):
        return " Empty"

    e2 = staticmethod(e2)

class ArmorConcreteDecorator():
    def __init__(self, character):
        self.character = character
        self.name = character.name
        self.a="\nArmor: Yes"

    @CharacterConcreteComponent.e2
    def equip(self):
        return self.character.a

class SwordConcreteDecorator():
    def __init__(self, character):
        self.character = character
        self.name = character.name
        self.a="\nSword: Yes"

    @CharacterConcreteComponent.e2
    def equip(self):
        return self.character.a

    
if __name__ == "__main__":
    main()