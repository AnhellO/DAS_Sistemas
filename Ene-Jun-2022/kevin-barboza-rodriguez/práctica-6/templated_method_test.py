import unittest
from templated_method import *

class worker_test(unittest.TestCase):

    def test_clase_worker(self):
        fire_fighter = FireFigther()
        self.assertIsInstance(fire_fighter, FireFigther)

        lumber_jack = LumberJack()
        self.assertIsInstance(lumber_jack, LumberJack)

        postman = Postman()
        self.assertIsInstance(postman, Postman)
        
        manager = Manager()
        self.assertIsInstance(manager,Manager)


    def test_override_method(self):

        fire_fighter = FireFigther()
        self.assertFalse(Worker.work(self), fire_fighter.work())

        lumber_jack = LumberJack()
        self.assertFalse(Worker.work(self), lumber_jack.work())

        postman = Postman()
        self.assertFalse(Worker.work(self), postman.work())
        
        manager = Manager()
        self.assertFalse(Worker.work(self), manager.work())

if __name__=="__main__":
    unittest.main()