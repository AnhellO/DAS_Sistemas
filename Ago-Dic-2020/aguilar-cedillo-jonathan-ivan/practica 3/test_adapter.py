import unittest
from adapter import Target, client_code


class TargetTest(unittest.TestCase):
    def test_target(self):
        target = Target()
        self.assertEqual(client_code(target), "Objetivo: comportamiento del objetivo predeterminado")

if __name__ == "__main__":
    unittest.main()