import unittest

# Change with the name of your module and funtions
from lib import hello

# Create all needed class for test


class TestHello(unittest.TestCase):
    def test_hello_output(self):
        self.assertEqual(hello.say_hello(), "Hello World!")
