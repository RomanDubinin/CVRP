from src.inside_customers_heuristics import hamiltonian_cycle_cheapest_insertion, get_partitioning, \
    tour_partitioning_heuristic

p = [(0,0,0), (10,10,0), (7,5,0), (4,1,0)]



h = tour_partitioning_heuristic((3,6,0),p, 2)
print(h)