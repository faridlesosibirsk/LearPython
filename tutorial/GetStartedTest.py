import unittest

from GetStarted import GetStarted
from GetStarted import sum


class TestGetStarted(unittest.TestCase):
    def test_helloworld(self):
        result = GetStarted()
        self.assertEqual(result, "Hello World!")


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
