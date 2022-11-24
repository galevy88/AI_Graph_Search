#Gal Levy 208540872
import Node_Functions


class Node:
    def __init__(self, state, path, path_cost):
        self.state = state
        self.object = Node_Functions.get_object(state_index=state)
        self.path = self.manage_path_addition(path)
        self.path_cost = path_cost

    def expand(self, f):
        obj = Node_Functions.get_object(self.state)
        children = []
        for l in obj.links:
            new_node_state, new_node_path, new_node_path_cost = Node_Functions.generate_payload_for_node(l.target, self.state, self.path, self.path_cost, l.distance, l.highway_type, f)
            children.append( Node(state=new_node_state, path=new_node_path, path_cost=new_node_path_cost) )
        return children

    def manage_path_addition(self, path):
        ls = []
        if path != None:
            for e in path:
                ls.append(e)
        return ls
    
    def get_lat_lon(self, state_index):
        return Node_Functions.get_lat_lon(state_index)
        