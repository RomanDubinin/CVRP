from operator import sub
from math import sqrt

def disstance(point1, point2):
    diff = tuple(map(sub, point1, point2))
    return sqrt(diff[0] * diff[0]+
                diff[1] * diff[1]+
                diff[2] * diff[2])