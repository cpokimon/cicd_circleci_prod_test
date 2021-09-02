import unittest
from main import hello_world


class ApiTestCase(unittest.TestCase):
    def test_hello_world_returns_hello_world(self):
        expected = "<p>Hello, World!</p>"
        self.assertEqual(expected, hello_world())


if __name__ == '__main__':
    unittest.main()
