from CharacterConcreteComponent import CharacterConcreteComponent
from ArmorConcreteDecorator import ArmorConcreteDecorator


class SwordConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f"{self.name} equipment:\nSword: Yes"
