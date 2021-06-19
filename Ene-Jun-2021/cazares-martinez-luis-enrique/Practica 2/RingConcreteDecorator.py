from CharacterConcreteComponent import CharacterConcreteComponent


class RingConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f'{self.name} equipment:\nRing: Yes'
