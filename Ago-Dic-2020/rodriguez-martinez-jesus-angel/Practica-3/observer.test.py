import unittest

from observer import Subscriber, Publisher

class SubscriberTest(unittest.TestCase):
    def test_subscriber_creation(self):
        sub = Subscriber("Bob")
        self.assertEqual(str(sub), "I'm Bob")

class PublisherTest(unittest.TestCase):
    def test_publisher_creation(self):
        pub = Publisher()
        bob = Subscriber("Bob")
        pub.register(bob)
        self.assertEqual(pub.dispatch("First update from publisher"), 'Bob got message: "First update from publisher"\n')

if __name__ == "__main__":
    unittest.main()
