
import Node_Functions


class Node:
    def __init__(self, state, path, path_cost, isAstar, end):
        self.state = state
        self.object = Node_Functions.get_object(state_index=state)
        self.path = self.manage_path_addition(path)
        self.path_cost = path_cost
        self.isAstar = isAstar
        self.end = end

    def expand(self, f):
        obj = Node_Functions.get_object(self.state)
        children = []
        for l in obj.links:
            if self.isAstar:
                new_node_state, new_node_path, new_node_path_cost = Node_Functions.generate_payload_for_node_Astar(l.target, self.state, self.path, self.path_cost, l.distance, l.highway_type, f, self.end)
            else:
                new_node_state, new_node_path, new_node_path_cost = Node_Functions.generate_payload_for_node(l.target, self.state, self.path, self.path_cost, l.distance, l.highway_type, f)
            children.append( Node(state=new_node_state, path=new_node_path, path_cost=new_node_path_cost, isAstar=self.isAstar, end = self.end) )
        return children

    def manage_path_addition(self, path):
        ls = []
        if path != None:
            for e in path:
                ls.append(e)
        return ls
        