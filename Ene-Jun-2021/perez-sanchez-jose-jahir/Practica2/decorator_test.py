import unittest

from decorator import CharacterConcreteComponent, SwordConcreteDecorator, ArmorConcreteDecorator, Character, RingConcreteDecorator, ShieldConcreteDecorator

class DecoratorTest(unittest.TestCase):
    def test_character_without_equipment(self):
        character = CharacterConcreteComponent(name='Luxor')
        self.assertEqual(
            character.equip(),
            "Luxor equipment: Empty"
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

    def test_character_with_shield(self):
        character = CharacterConcreteComponent(name='Luxor')
        shield = ShieldConcreteDecorator(character)
        self.assertEqual(
            shield.equip(),
            "Luxor equipment:\nShield: Yes"
        )


if __name__ == "__main__":
    unittest.main()