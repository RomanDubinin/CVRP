from src.full_search import get_all_partitions
from itertools import permutations
from math import sqrt
from operator import sub

from src.graph_visualize import visualize


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


def get_optimal_salesman_tour(depos, set_of_customers):
    min_toir_len = float("inf")
    optimal_tour = ()

    for permutation in permutations(set_of_customers):
        for depo in depos:
            tour_len = get_tour_len(depo, permutation)

            if tour_len < min_toir_len:
                min_toir_len = tour_len
                optimal_tour = permutation
                optimal_depo = depo

        return (optimal_depo, optimal_tour)

depos = [
         (5,5,0),
    (0,0,0),
         # (0,5,0),
         (4,0,0)
         ]

customers = [(1,0,0),
             (2,1.5,0),
             # (2,0.5,0),
             # (2,3,0),
             # (0,4,0),
             # (5,4,0),
             (4,4,0)]

q = 2


partitions = get_all_partitions(set(customers), q)
optimal_solution = []
min_solution_len = float("inf")

for partition in partitions:
    solution = []

    for subset in partition:
        optimal_depo, optimal_tour = get_optimal_salesman_tour(depos, subset)
        solution.append((optimal_depo, optimal_tour))

    solution_len = sum([get_tour_len(elem[0], elem[1]) for elem in solution])

    if solution_len < min_solution_len:
        min_solution_len = solution_len
        optimal_solution = solution

for tour in optimal_solution:
    print(tour)

#######################################


customer_nodes = []
for tour in optimal_solution:
    for customer in tour[1]:
        customer_nodes.append({"name": customer, "group": depos.index(tour[0]), "coords": customer})
print(customer_nodes)

depo_nodes = []
for depo in depos:
    depo_nodes.append({"name": depo, "group": depos.index(depo), "coords": depo})
print(depo_nodes)

edges = []
for tour in optimal_solution:
    edges.append({"source":tour[0], "target": tour[1][0]})
    edges.append({"source":tour[1][-1], "target": tour[0]})
    for i in range(len(tour[1]) - 1):
        edges.append({"source": tour[1][i], "target": tour[1][i+1]})

visualize(depo_nodes, customer_nodes, edges)