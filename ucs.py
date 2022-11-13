import pQueue
from ways.graph import Roads
from ways.graph import load_map_from_csv
from ways.tools import compute_distance
from Node import Node


def best_first_graph_search(start, end):
    frontier = pQueue.pQueue()
    start_node = Node(start, [], 0)
    frontier.append_node(start_node)
    close_list = set()
    while frontier.isNotEmpty():
        frontier.sort_pQueue()
        current_node = frontier.pop()
        if current_node.state == end:
            print(f"I FOUND: {current_node.state} CURRENT NODE PATH: {current_node.path}")
            return current_node
        close_list.add(current_node.state)
        for child in current_node.expand():
            if child.state not in close_list and not frontier.check_if_node_in_frontier(child):
                frontier.append_node(child)
            else:
                frontier.find_problematic_child(child)
    return None


def uniform_cost_search(start, end):
   return best_first_graph_search(start, end)

