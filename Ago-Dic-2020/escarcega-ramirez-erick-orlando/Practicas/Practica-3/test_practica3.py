import unittest
from practica3 import Proxy,Reservation,ReservationService,User,StatsService,Ex

class test(unittest.TestCase):

    def test_Ex_Pass(self):
        user = "John the Admin"
        year = 2017

        self.assertEqual(Ex(User(True,user), year), 'John the Admin will see: 50.0')

    def test_Ex_Denied(self):
        user = "Guest"
        year = 2017

        self.assertEqual(Ex(User(False,user), year), 'Guest will see: 0')

if __name__ == "__main__":
    unittest.main()