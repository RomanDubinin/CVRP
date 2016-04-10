from operator import sub
from math import sqrt

def disstance(point1, point2):
    diff = tuple(map(sub, point1, point2))
    return sqrt(diff[0] * diff[0]+
                diff[1] * diff[1]+
                diff[2] * diff[2])

def get_tour_len(depo, customers):
    sum_ = 0
    for i in range(len(customers)-1):
        sum_ += disstance(customers[i], customers[i+1])

    sum_ = sum_ + disstance(depo, customers[0]) + disstance(customers[-1], depo)

    return sum_