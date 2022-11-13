'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

from BFGS import best_first_graph_search
from ways.tools import calculate_distance

def huristic_function(lat1, lon1, lat2, lon2):

    raise NotImplementedError


def find_ucs_rout(source, target):
    best_first_graph_search(source, target, calculate_distance)

def batch_find_ucs_rout(source, target):
    node_payload = best_first_graph_search(source, target, calculate_distance)
    node_state = node_payload.state
    node_path = node_payload.path
    node_path_cost = node_payload.path_cost
    node_path.append(node_state)
    
    return source, target, node_path, node_path_cost

def find_astar_route(source, target):
    'call function to find path, and return list of indices'
    raise NotImplementedError


def find_idastar_route(source, target):
    'call function to find path, and return list of indices'
    raise NotImplementedError
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    # from sys import argv
    # dispatch(argv)
    print("Got you!")
    source = 606320
    target = 5303
    find_ucs_rout(source, target)
