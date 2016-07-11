import unittest
from question2 import perfectCity


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(2.7, perfectCity([0.4, 1], [0.9, 3]))

    def test_2(self):
        self.assertEqual(8.9, perfectCity([2.4, 1], [5, 7.3]))

    def test_3(self):
        self.assertEqual(7.7, perfectCity([0, 0.2], [7, 0.5]))

    def test_4(self):
        self.assertEqual(2, perfectCity([0, 0.4], [1, 0.6]))
