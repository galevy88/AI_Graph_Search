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

def generate_payload_for_node(state, father_state, path, father_path_cost, distance):
    new_node_state = state
    new_node_path = []
    if path != None:
        for e in path:
            new_node_path.append(e)
    new_node_path.append(father_state)
    # child_lat, child_lon = get_lat_lon(new_node_state)
    # curent_node_lat, current_node_lon = get_lat_lon(father_state)
    # new_node_path_cost = f(child_lat, child_lon, curent_node_lat, current_node_lon)
    # print(f"New_node_state: {new_node_state} New_node_path: {new_node_path} new_node_path_cost: {new_node_path_cost}")
    new_node_path_cost = father_path_cost + distance
    return new_node_state, new_node_path, new_node_path_cost