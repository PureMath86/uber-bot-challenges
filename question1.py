"""
Uber is building a Fare Estimator that can tell you how much your ride will cost before you request it.

It works by passing approximated ride distance and ride time through this formula:
`(Cost per minute) * (ride time) + (Cost per mile) * (ride distance)`

where Cost per minute and Cost per mile depend on the car type.

You are one of the engineers building the Fare Estimator, so knowing cost per minute and cost per mile
for each car type, as well as ride distance and ride time, return the fare estimates for all car types.

Example:

ride_time = 30,
ride_distance = 7,
cost_per_minute = [0.2, 0.35, 0.4, 0.45] and
cost_per_mile = [1.1, 1.8, 2.3, 3.5], the output should be

fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile) = [13.7, 23.1, 28.1, 38]
"""


def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    fares = [0]*len(cost_per_mile)
    for i in xrange(len(cost_per_mile)):
        fare = cost_per_minute[i]*ride_time + cost_per_mile[i]*ride_distance
        fares[i] = float("{:.1f}".format(fare))
    return fares

