import unittest

from Decorator import *

class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment:"
        )
    def test_character_with_armor(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        self.assertEqual(
            armor.equip(),
            "Luxor equipment:\nArmor: Yes"
        )
    def test_character_with_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        sword = SwordConcreteDecorator(character)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nSword: Yes"
        )
    def test_character_with_armor_and_sword(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        self.assertEqual(
            sword.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes"
        )
    def test_character_with_ring(self):
        character = CharacterConcreteComponent(name='Luxor')
        ring = RingConcreteDecorator(character)
        self.assertEqual(
            ring.equip(),
            "Luxor equipment:\nRing: Yes"
        )
    def test_character_with_necklace(self):
        character = CharacterConcreteComponent(name='Luxor')
        necklace = NecklaceConcreteDecorator(character)
        self.assertEqual(
            necklace.equip(),
            "Luxor equipment:\nNecklace: Yes"
        )
    def test_character_with_all(self):
        character = CharacterConcreteComponent(name='Luxor')
        armor = ArmorConcreteDecorator(character)
        sword = SwordConcreteDecorator(armor)
        ring = RingConcreteDecorator(sword)
        necklace = NecklaceConcreteDecorator(ring)
        self.assertEqual(
            necklace.equip(),
            "Luxor equipment:\nArmor: Yes\nSword: Yes\nRing: Yes\nNecklace: Yes"
        )




if __name__ == '__main__':
    unittest.main()