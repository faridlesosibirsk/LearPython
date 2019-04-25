import unittest

from helloworld import helloworld


class TestHelloworld(unittest.TestCase):
    def test_helloworld(self):
        result = helloworld()
        self.assertEqual(result, "Hello, World!")


if __name__ == '__main__':
    unittest.main()
