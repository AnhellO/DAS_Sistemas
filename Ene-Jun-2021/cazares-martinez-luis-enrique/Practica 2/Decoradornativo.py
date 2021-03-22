class CharacterConcreteComponent:

    def __init__(self, name):
        self.name = name

    def equip(self):
        return f'{self.name} equipment: Empty'


class ArmorConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f"{self.name} equipment:\nArmor: Yes"


class SwordConcreteDecorator(CharacterConcreteComponent):

    def equip(self):
        return f"{self.name} equipment:\nSword: Yes"


def ArmorConcreteDecoratorr(func):

    def agregaarmadura():
        func()
        print(f'Luxor equipment:\nArmor: Yes')

    return agregaarmadura()


def SwordConcreteDecoratorr(func):

    def agregaespada():
        func()
        print(f'Luxor equipment:\nSword: Yes')

    return agregaespada()


@ArmorConcreteDecoratorr
def ArmorConcreteDecorator():
    CharacterConcreteComponent(name='Luxor').equip()


@SwordConcreteDecoratorr
def SwordConcreteDecorator():
    CharacterConcreteComponent(name='Luxor').equip()


def main():
    personajeBase = CharacterConcreteComponent(name='Luxor')
    equipoBase = personajeBase.equip()

    personjaArmadura = ArmorConcreteDecorator(personajeBase.name)
    equipoArmadura = personjaArmadura.equip()

    print(equipoBase)
    print(equipoArmadura)


if __name__ == '__main__':
    main()
