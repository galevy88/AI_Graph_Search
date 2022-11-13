from ways.graph import Roads
from ways.graph import load_map_from_csv
from ways.tools import compute_distance

graph = Roads(load_map_from_csv())

def get_object(state_index):
    obj = graph.junctions()[state_index]
    return obj

def get_lat_lon(state_index):
    obj = graph.junctions()[state_index]
    return obj.lat, obj.lon

def generate_payload_for_node(state, father_state, path, father_path_cost, distance, f):
    new_node_state = state
    new_node_path = []
    if path != None:
        for e in path:
            new_node_path.append(e)
    new_node_path.append(father_state)
    new_node_path_cost = f(father_path_cost, distance)
    return new_node_state, new_node_path, new_node_path_cost