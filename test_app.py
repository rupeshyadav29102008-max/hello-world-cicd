import unittest
from app import hello_world
class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")#for DevOps lab
    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)
    def test_welcome_message(self):
        self.assertEqual(welcome_message("Alice"), "Welcome to DevOps, Rupesh!")
        self.assertEqual(welcome_message("Bob"), "Welcome to DevOps, Naman!")
if __name__ == "__main__":
    unittest.main()
