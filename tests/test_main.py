import unittest

from app.main import print_greeting


class TestGreeting(unittest.TestCase):
    def test_print_greeting(self):
        self.assertEqual(print_greeting(), "Hello, World!")

    def test_greeting_type(self):
        self.assertIsInstance(print_greeting(), str)


if __name__ == "__main__":
    unittest.main()
