
import Node_Functions


class Node:
    def __init__(self, state, path, path_cost, f):
        self.state = state
        self.object = Node_Functions.get_object(state_index=state)
        self.path = self.manage_path_addition(path)
        self.path_cost = path_cost
        self.f = f

    def expand(self):
        obj = Node_Functions.get_object(self.state)
        children = []
        for l in obj.links:
            new_node_state, new_node_path, new_node_path_cost = Node_Functions.generate_payload_for_node(l.target, self.state, self.path, self.f)
            children.append( Node(state=new_node_state, path=new_node_path, path_cost=new_node_path_cost, f=self.f) )
        return children

    def manage_path_addition(self, path):
        ls = []
        if path != None:
            for e in path:
                ls.append(e)
        return ls
        