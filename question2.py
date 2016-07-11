"""
Consider a city where the streets are perfectly laid out to form an infinite square grid.
In this city finding the shortest path between two given points (an origin and a destination)
is much easier than in other more complex cities.

As a new Uber developer, you are tasked to create an algorithm that does this calculation.

Given user's departure and destination coordinates, each of them located on some street,
find the length of the shortest route between them assuming that cars can only move along the streets.

Example

For departure = [0.4, 1] and destination = [0.9, 3], the output should be
perfectCity(departure, destination) = 2.7.
"""


def distance(a, b):
    return abs(a-b)


def find_abs_diff(new_corner, original):
    return distance(new_corner[0], original[0]), distance(new_corner[1], original[1])


def find_new_corner_coord(departure_coord, destination_coord):
    if int(departure_coord) == int(destination_coord):
        if distance(departure_coord, int(departure_coord)+1) < 0.5 or \
                distance(destination_coord, int(destination_coord)+1) < 0.5:
            return int(departure_coord)+1
        else:
            return int(departure_coord)
    elif departure_coord < destination_coord:  # go +
        return int(departure_coord)+1
    else:  # go -
        return int(departure_coord)


def find_new_corner(original_corner, target_node):
    return find_new_corner_coord(original_corner[0], target_node[0]), \
           find_new_corner_coord(original_corner[1], target_node[1])


def perfectCity(departure, destination):
    # Find appropriate corner node for departure
    depart_corner = find_new_corner(departure, destination)
    depart_abs_diff = find_abs_diff(depart_corner, departure)

    # Find appropriate corner node for destination
    dest_corner = find_new_corner(destination, depart_corner)
    dest_abs_diff = find_abs_diff(dest_corner, destination)

    # Distance btw 2 corner nodes
    corners_dist = distance(depart_corner[0], dest_corner[0]) + distance(depart_corner[1], dest_corner[1])

    # Total Distance
    total_dist = depart_abs_diff[0] + depart_abs_diff[1] + dest_abs_diff[0] + dest_abs_diff[1] + corners_dist

    return float("{0:.1f}".format(total_dist))

