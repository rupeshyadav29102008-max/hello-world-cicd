import unittest
from app import hello_world, welcome_message
class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(hello_world(), "Hello, DevOps!")#for DevOps lab
    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)
    def test_welcome_message(self):
        self.assertEqual(welcome_message("Rupesh"), "Welcome to DevOps, Rupesh!")
        self.assertEqual(welcome_message("Naman"), "Welcome to DevOps, Naman!")
if __name__ == "__main__":
    unittest.main()
