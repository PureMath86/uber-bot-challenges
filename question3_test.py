import unittest
from question3 import parkingSpot


class TestCase(unittest.TestCase):

    def test_1(self):
        carDimensions = [3, 2]
        parkingLot = [[1,0,1,0,1,0],
         [0,0,0,0,1,0],
         [0,0,0,0,0,1],
         [1,0,1,1,1,1]]
        luckySpot =[1, 1, 2, 3]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_2(self):
        carDimensions = [3, 2]
        parkingLot =[
            [1,0,1,0,1,0],
            [1,0,0,0,1,0],
            [0,0,0,0,0,1],
            [1,0,0,0,1,1]
        ]
        luckySpot = [1, 1, 2, 3]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_3(self):
        carDimensions = [4, 1]
        parkingLot = [
            [1,0,1,0,1,0],
            [1,0,0,0,1,0],
            [0,0,0,0,0,1],
            [1,0,0,0,1,1]
        ]
        luckySpot = [0, 3, 3, 3]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_4(self):
        carDimensions = [2, 1]
        parkingLot = [[1,0,1],
         [1,0,1],
         [1,1,1]]
        luckySpot = [0, 1, 1, 1]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_5(self):
        carDimensions = [4, 2]
        parkingLot = [[0,0,0,1],
         [0,0,0,0],
         [0,0,1,1]]
        luckySpot = [0, 0, 1, 3]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_6(self):
        carDimensions = [7, 2]
        parkingLot = [[0,1,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]
        luckySpot = [1, 0, 7, 1]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_7(self):
        carDimensions = [5, 3]
        parkingLot = [[1,1,1,1,1,0,1,1,1,1],
         [0,1,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,1,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0]]
        luckySpot = [1, 3, 5, 5]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_8(self):
        carDimensions =[2, 1]
        parkingLot = [[1,0,1],
         [1,0,1],
         [1,1,1]]
        luckySpot =[1, 1, 2, 1]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_9(self):
        carDimensions = [2, 1]
        parkingLot = [[1,1,1],
         [1,0,1],
         [1,0,1]]
        luckySpot = [0, 1, 1, 1]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_10(self):
        carDimensions = [2, 1]
        parkingLot = [[1,1,1,1],
         [1,0,0,0],
         [1,0,1,0]]
        luckySpot = [2, 1, 2, 2]
        self.assertFalse(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_11(self):
        carDimensions = [2, 1]
        parkingLot = [[1,1,1,1],
         [1,0,0,0],
         [1,0,1,0]]
        luckySpot = [1, 2, 1, 3]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

    def test_12(self):
        carDimensions = [7, 2]
        parkingLot = [[0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]]
        luckySpot = [1, 1, 2, 7]
        self.assertTrue(parkingSpot(carDimensions, parkingLot, luckySpot))

