
# you have a function called random that generates a number from 0 - 1 uniformly. calculate the value of Pi
import random


def findPi(n):
    # get the total number of points
    # // Get the total number of points in the circles
    # get pi giver PIr**2/(2pi)**2
    num_point_cirle = 0
    num_point_square = 0
    for i in range(n):
        y = random.uniform(0, 1)
        x = random.uniform(
            0, 1
        )
        distance = x**2 + y**2
        if distance <= 1:
            num_point_cirle += 1

        num_point_square += 1
    return 4 * (num_point_cirle/num_point_square)


print(findPi(20000000))
