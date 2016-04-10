from src.common import disstance, get_tour_len
from src.Node import Node

def incertion_price_recount(incert_infos, last_added_node, left_node, right_node):
    for point in incert_infos:
        possible_new_price = disstance(left_node.value, point) + \
                             disstance(point, last_added_node.value) - \
                             disstance(left_node.value, last_added_node.value)
        if possible_new_price < incert_infos[point]["price"]:
            incert_infos[point]["price"] = possible_new_price
            incert_infos[point]["place"] = (left_node, last_added_node)

        possible_new_price = disstance(last_added_node.value, point) + \
                             disstance(point, right_node.value) - \
                             disstance(last_added_node.value, right_node.value)
        if possible_new_price < incert_infos[point]["price"]:
            incert_infos[point]["price"] = possible_new_price
            incert_infos[point]["place"] = (last_added_node, right_node)

def incert(left_node, right_node, value):
    new_node = Node(value, right_node)
    left_node.next = new_node
    return new_node

def linked_list_to_list(first_node):
    first_val = first_node.value
    res = [first_val]
    current_station = first_node.next
    while current_station != first_node:
        res.append(current_station.value)
        current_station = current_station.next

    return res

def get_cheapest_price(incert_infos):
    min_price = float("inf")

    for key in incert_infos:
        if incert_infos[key]["price"] < min_price:
            min_price = incert_infos[key]["price"]
            cheapest = incert_infos[key]
    return cheapest

def hamiltonian_cycle_cheapest_insertion(points):
    first_node = Node(points[0], None)
    second_node = Node(points[1], None)

    first_node.next = second_node
    second_node.next = first_node

    points.remove(first_node.value)
    points.remove(second_node.value)

    last_added = second_node
    left_neighbour = first_node
    right_neighbour = first_node

    incert_infos = {}
    for point in points:
        incert_infos[point] = {"point": point, "price": float("inf"), "place": (first_node, second_node)}


    while len(incert_infos) > 0:
        incertion_price_recount(incert_infos, last_added, left_neighbour, right_neighbour)
        cheapest = get_cheapest_price(incert_infos)

        left_neighbour, right_neighbour = cheapest["place"]
        last_added = incert(left_neighbour, right_neighbour, cheapest["point"])

        incert_infos.pop(cheapest["point"])

    return linked_list_to_list(last_added)


def get_all_shifts(list_):
    res = []
    for i in range(len(list_)):
        res.append(list_[i:] + list_[:i])

    return res

def get_partitioning(list_, n):
    partition = []
    for i in range(0, len(list_), n):
        partition.append(list_[i:i + n])

    return partition

def calculate_partitioning_len(depo, partition):
    return sum([get_tour_len(depo, part) for part in partition])

def tour_partitioning_heuristic(depo, points, capacity):
    hamiltonian_cycle = hamiltonian_cycle_cheapest_insertion(points)
    partition = get_partitioning(hamiltonian_cycle, capacity)
    min_partitiining_len = calculate_partitioning_len(depo, partition)

    for shift in get_all_shifts(hamiltonian_cycle):
        partition = get_partitioning(shift, capacity)
        partitiining_len = calculate_partitioning_len(depo, partition)
        if partitiining_len < min_partitiining_len:
            optimal_partition = partition

    return optimal_partition