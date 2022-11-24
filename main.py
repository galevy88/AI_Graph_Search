#Gal Levy 208540872
'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

from BFGS import best_first_graph_search
from IDA import IDA
from distance_functions import cost_function, huristic_function
from ways.graph import load_map_from_csv
from ways.draw import plot_path

def fetch_results_from_node_payload(node_payload):
    node_state = node_payload.state
    node_path = node_payload.path
    node_path_cost = node_payload.path_cost
    node_path.append(node_state)
    return node_path, node_path_cost

def find_ucs_rout(source, target):
    node_payload = best_first_graph_search(source, target, cost_function)
    node_path, node_path_cost = fetch_results_from_node_payload(node_payload)
    return source, target, node_path, node_path_cost

def find_astar_route(source, target):
    node_payload = best_first_graph_search(source, target, cost_function, huristic_function)
    node_path, node_path_cost = fetch_results_from_node_payload(node_payload)
    return source, target, node_path, node_path_cost


def find_idastar_route(source, target):
    node_payload = IDA(source, target)
    node_path, node_path_cost = fetch_results_from_node_payload(node_payload)
    return source, target, node_path, node_path_cost
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path[2]))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
