import unittest

from videogame import EquipArmor, EquipSword, EquipArmorSword, EquipShield, EquipFlamethrower, Human, Robot

class VideoGameTest(unittest.TestCase):
    def test_robot_with_armor_and_sword(self):
        robot = EquipArmorSword(Robot())
        
        self.assertIsInstance(robot.show(), str)
        self.assertEqual('Selected robot with armor and sword', robot.show())

    def test_robot_with_sword(self):
        robot = EquipSword(Robot()).show()

        self.assertIsInstance(robot, str)
        self.assertEqual(
            'Selected robot with sword',
            str(robot)
        )

    def test_robot_with_shield(self):
        robot = EquipShield(Robot()).show()

        self.assertIsInstance(robot, str)
        self.assertEqual(
            'Selected robot with shield',
            str(robot)
        )

    def test_robot_with_flamethrower(self):
        robot = EquipFlamethrower(Robot()).show()

        self.assertIsInstance(robot, str)
        self.assertEqual(
            'Selected robot with flamethrower',
            str(robot)
        )

    def test_human_with_armor_and_sword(self):
        human = EquipArmorSword(Human()).show()

        self.assertIsInstance(human, str)
        self.assertEqual(
            'Selected human with armor and sword',
            str(human)
        )

    def test_human_with_armor(self):
        human = EquipArmor(Human()).show()

        self.assertIsInstance(human, str)
        self.assertEqual(
            'Selected human with armor',
            str(human)
        )

    def test_human_with_sword(self):
        human = EquipSword(Human()).show()

        self.assertIsInstance(human, str)
        self.assertEqual(
            'Selected human with sword',
            str(human)
        )

    def test_human_with_shield(self):
        human = EquipShield(Human()).show()

        self.assertIsInstance(human, str)
        self.assertEqual(
            'Selected human with shield',
            str(human)
        )

    def test_human_with_flamethrower(self):
        human = EquipFlamethrower(Human()).show()

        self.assertIsInstance(human, str)
        self.assertEqual(
            'Selected human with flamethrower',
            str(human)
        )

if __name__ == "__main__":
    unittest.main()