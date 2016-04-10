from src.common import disstance
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
        min_price = float("inf")
        for key in incert_infos:
            if incert_infos[key]["price"] < min_price:
                min_price = incert_infos[key]["price"]
                cheapest = incert_infos[key]



        left_neighbour, right_neighbour = cheapest["place"]
        last_added = Node(cheapest["point"], right_neighbour)
        left_neighbour.next = last_added

        incert_infos.pop(cheapest["point"])


    first_point = last_added.value
    res = [first_point]
    current_station = last_added.next
    while current_station.value != first_point:
        res.append(current_station.value)
        current_station = current_station.next

    return res
