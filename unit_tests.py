import unittest

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(0, 0), 0)

    def test_2(self):
        self.assertEqual(add(0, 1), 1)

    def test_3(self):
        self.assertEqual(add(1, 0), 1)

def add(a, b):
    return a + b

if __name__ == '__main__':
    unittest.main()
