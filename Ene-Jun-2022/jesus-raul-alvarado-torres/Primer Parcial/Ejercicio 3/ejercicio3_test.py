import unittest
from ejercicio3 import director

test_cases = [
    {
        'name': 'triangle ok',
        'input': 'triangle',
        'expected_output': 'I am a triangle!',
    },
    {
        'name': 'square ok',
        'input': 'square',
        'expected_output': 'I am a square!',
    },
    {
        'name': 'pentagon ok',
        'input': 'pentagon',
        'expected_output': 'I am a pentagon!',
    }
]

class Test_Factory_Method(unittest.TestCase):
    def test_polygon(self) -> None:
        for test in test_cases:
            self.assertEqual(director(test['input']), test['expected_output'])

if __name__ == '__main__':
    unittest.main()