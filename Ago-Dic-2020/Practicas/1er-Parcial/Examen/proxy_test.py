import unittest

from proxy import *

class ProxyTest(unittest.TestCase):
    def test_level_one_user(self):
        usr = User(name='foo', access_level=1)
        proxy = SystemAuthProxy(usr, "Payments")
        self.assertEqual("User 'foo' is doing level-1 tasks on system ### Payments ###", proxy.level_1_tasks())
        self.assertEqual("ERROR: User 'foo' is not authorized to do level-2 tasks", proxy.level_2_tasks())
        self.assertEqual("ERROR: User 'foo' is not authorized to do level-3 tasks", proxy.level_3_tasks())
    
    def test_level_two_user(self):
        usr = User(name='bar', access_level=2)
        proxy = SystemAuthProxy(usr, "IT")
        self.assertEqual("User 'bar' is doing level-1 tasks on system ### IT ###", proxy.level_1_tasks())
        self.assertEqual("User 'bar' is doing level-2 tasks on system ### IT ###", proxy.level_2_tasks())
        self.assertEqual("ERROR: User 'bar' is not authorized to do level-3 tasks", proxy.level_3_tasks())
    
    def test_level_three_user(self):
        usr = User(name='baz', access_level=3)
        proxy = SystemAuthProxy(usr, "Sales")
        self.assertEqual("User 'baz' is doing level-1 tasks on system ### Sales ###", proxy.level_1_tasks())
        self.assertEqual("User 'baz' is doing level-2 tasks on system ### Sales ###", proxy.level_2_tasks())
        self.assertEqual("User 'baz' is doing level-3 tasks on system ### Sales ###", proxy.level_3_tasks())
    

if __name__ == "__main__":
    unittest.main()
