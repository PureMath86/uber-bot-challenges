"""
This time you are an Uber driver and you are trying your best to park your car in a parking lot.

Your car has length carDimensions[0] and width carDimensions[1].
You have already picked your lucky spot (rectangle of the same size as the car with upper left corner
at (luckySpot[0], luckySpot[1])) and bottom right corner at (luckySpot[2], luckySpot[3])
and you need to find out if it's possible to park there or not.

It is possible to park your car at a given spot if and only if
you can drive through the parking lot without any turns to your lucky spot
(for safety reasons, the car can only move in two directions inside the parking lot
- forwards or backwards along the long side of the car) starting from some side of the lot.

Assume that the car can't drive through or park at any of the occupied spots.

Example

For carDimensions = [3, 2],

parkingLot = [[1, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1],
              [1, 0, 1, 1, 1, 1]]
and
luckySpot = [1, 1, 2, 3], the output should be
parkingSpot(carDimensions, parkingLot, luckySpot) = true.
"""


def is_left_entrance_clear(parkingLot, luckySpot):
    nodes_to_check = []
    x = luckySpot[0]
    while x <= luckySpot[2]: # on same row
        y = luckySpot[1]-1
        while y >= 0:
            nodes_to_check.append((x, y))
            y -= 1
        x += 1
    for x, y in nodes_to_check:
        if parkingLot[x][y] == 1:
            return False
    return True


def is_right_entrance_clear(parkingLot, luckySpot):
    nodes_to_check = []
    x = luckySpot[2]
    while x < len(parkingLot[0]): # on same row
        y = luckySpot[3]+1
        while y < len(parkingLot[0]):
            nodes_to_check.append((x, y))
            y += 1
        x += 1
    for x, y in nodes_to_check:
        if parkingLot[x][y] == 1:
            return False
    return True


def is_up_entrance_clear(parkingLot, luckySpot):
    nodes_to_check = []
    x = luckySpot[0]-1
    while x >= 0: # on same row
        y = luckySpot[1]
        while y <= luckySpot[3]:
            nodes_to_check.append((x, y))
            y += 1
        x -= 1
    for x, y in nodes_to_check:
        if parkingLot[x][y] == 1:
            return False
    return True


def is_down_entrance_clear(parkingLot, luckySpot):
    nodes_to_check = []
    x = luckySpot[2]+1
    while x < len(parkingLot): # on same row
        y = luckySpot[1]
        while y <= luckySpot[3]:
            nodes_to_check.append((x, y))
            y += 1
        x += 1
    for x, y in nodes_to_check:
        if parkingLot[x][y] == 1:
            return False
    return True


def define_spot_orientation(luckySpot):
    if abs(luckySpot[1]-luckySpot[3]) > abs(luckySpot[0]-luckySpot[2]):
        return "horizontal"
    else:
        return "vertical"


def is_entrance_exist(parkingLot, luckySpot):
    if define_spot_orientation(luckySpot) == "horizontal":
        return is_left_entrance_clear(parkingLot, luckySpot) or is_right_entrance_clear(parkingLot, luckySpot)
    else: # spot orientation "vertical"
        return is_up_entrance_clear(parkingLot, luckySpot) or is_down_entrance_clear(parkingLot, luckySpot)


def is_lucky_spot_empty(parkingLot, luckySpot):
    x = luckySpot[0]
    while x <= luckySpot[2]:
        y = luckySpot[1]
        while y <= luckySpot[3]:
            if parkingLot[x][y] == 1:
                return False
            y += 1
        x += 1
    return True


def is_spot_fit_car(carDimensions, luckySpot):
    return carDimensions[0] > luckySpot[2] - luckySpot[0] or carDimensions[1] > luckySpot[3] - luckySpot[1]


def parkingSpot(carDimensions, parkingLot, luckySpot):
    # Make sure the car can fit the spot
    if not is_spot_fit_car(carDimensions, luckySpot):
        return False

    # Make sure the spot is empty
    if not is_lucky_spot_empty(parkingLot, luckySpot):
        return False

    # Make sure there is a free entry large enough to the spot
    if not is_entrance_exist(parkingLot, luckySpot):
        return False

    return True
