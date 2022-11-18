import pQueue
from Node import Node


def best_first_graph_search(start, end, f, isAstar):
    frontier = pQueue.pQueue()
    start_node = Node(start, [], 0, isAstar, end)
    frontier.append_node(start_node)
    close_list = set()
    while frontier.isNotEmpty():
        frontier.sort_pQueue()
        current_node = frontier.pop()
        if current_node.state == end:
            return current_node
        close_list.add(current_node.state)
        for child in current_node.expand(f):
            if child.state not in close_list and not frontier.check_if_node_in_frontier(child):
                frontier.append_node(child)
            else:
                frontier.find_problematic_child(child)
    return None


