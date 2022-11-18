'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

from BFGS import best_first_graph_search
from ways.tools import compute_distance

def cost_function(x, y, speed):
    return ((x+y) / 1000) / speed

def huristic_function(lat1, lon1, lat2, lon2, max_speed):
    return compute_distance(lat1, lon1, lat2, lon2) / max_speed

def Astar_cost_function(x, y, lat1, lon1, lat2, lon2, speed, max_speed):
    return cost_function(x,y, speed) + huristic_function(lat1, lon1, lat2, lon2, max_speed)

def find_ucs_rout(source, target):
    node_payload = best_first_graph_search(source, target, cost_function, isAstar = False)
    node_state = node_payload.state
    node_path = node_payload.path
    node_path_cost = node_payload.path_cost
    node_path.append(node_state)
    return source, target, node_path, node_path_cost

def find_astar_route(source, target):
    node_payload = best_first_graph_search(source, target, Astar_cost_function, isAstar = True)
    node_state = node_payload.state
    node_path = node_payload.path
    node_path_cost = node_payload.path_cost
    node_path.append(node_state)
    return source, target, node_path, node_path_cost


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
    source = 17869
    target = 17867
    x = find_ucs_rout(source, target)
    y = find_astar_route(source, target)
    print(x)
    print(y)
