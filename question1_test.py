import unittest
from question1 import fareEstimator


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fareEstimator(30, 7, [0.2, 0.35, 0.4, 0.45], [1.1, 1.8, 2.3, 3.5]), [13.7, 23.1, 28.1, 38])

