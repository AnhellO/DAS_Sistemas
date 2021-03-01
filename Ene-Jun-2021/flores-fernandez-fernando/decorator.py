import abc
#inteface Component
class ICharacterComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def equip(self):
        pass
    
# Concrete Component
class CharacterConcreteComponent(ICharacterComponent):
    def __init__(self,name):
        self._name = name
    
    def equip(self):
        return f"{self._name} equipment: Empty"
    
# Base Decorator 
class CharacterDecorator(ICharacterComponent, metaclass=abc.ABCMeta):
    def __init__(self,character_component: ICharacterComponent):
        self._character_component = character_component
        
        @abc.abstractmethod
        def equip(self):
            pass
    
# Concrete Decorator: A
class ArmorConcreteDecorator(CharacterDecorator):
    def equip(self):
        if ( " Empty" in self._character_component.equip()):
            return f"{self._character_component.equip()[0:-6]}\nArmor: Yes"
        return f"{self._character_component.equip()}\nArmor: Yes"
# Concrete Decorator: B
class SwordConcreteDecorator(CharacterDecorator):
    def equip(self):
        if ( " Empty" in self._character_component.equip()):
            return f"{self._character_component.equip()[0:-6]}\nSword: Yes"
        return f"{self._character_component.equip()}\nSword: Yes"

# Concrete Decorator: C
class StaffConcreteDecorator(CharacterDecorator):
    def equip(self):
        if ( " Empty" in self._character_component.equip()):
            return f"{self._character_component.equip()[0:-6]}\nStaff: Yes"
        return f"{self._character_component.equip()}\nStaff: Yes"   
    
# Concrete Decorator: D
class MedallionConcreteDecorator(CharacterDecorator):
    def equip(self):
        if ( " Empty" in self._character_component.equip()):
            return f"{self._character_component.equip()[0:-6]}\nMedallion: Yes"
        return f"{self._character_component.equip()}\nMedallion: Yes"    
def main():
    character = CharacterConcreteComponent(name = "Luxor")
    armor = ArmorConcreteDecorator(character)
    p = armor.equip()
    
   
    print(p)
    
if __name__ == '__main__':
    main()    


        
       

    