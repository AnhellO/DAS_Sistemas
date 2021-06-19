from CharacterConcreteComponent import CharacterConcreteComponent


class ArmorConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f"{self.name} equipment:\nArmor: Yes"
