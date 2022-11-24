#Gal Levy 208540872
import Node_Functions

class pQueue:

    def __init__(self, end):
        self.frontier = []
        self.size = 0
        self.end_lat = Node_Functions.get_object(end).lat
        self.end_lon = Node_Functions.get_object(end).lon
    
    def append_node(self, node):
        self.frontier.append(node)
        self.size += 1

    def sort_pQueue(self):
        self.frontier.sort(key=lambda x: x.path_cost)

    def pop(self):
        pop = self.frontier[0]
        self.frontier.pop(0)
        return pop

    def isNotEmpty(self):
        if self.frontier:
            return True
        else:
            return False
    
    def check_if_node_in_frontier(self, node):
        for n in self.frontier:
            if node.state == n.state:
                return True
            else:
                return False
    
    def find_problematic_child_ucs(self, node):
        for n in self.frontier:
            if node.state == n.state:
                if node.path_cost < n.path_cost:
                    self.frontier.remove(n)
                    self.append_node(node)
                    print("CHANGE OCCUR!")
    
    def find_problematic_child_astar(self, node, h):
        for n in self.frontier:
            if node.state == n.state:
                lat1, lon1 = node.get_lat_lon(node.state)
                lat2, lon2 = n.get_lat_lon(n.state)
                if node.path_cost + h(lat1,lon1, self.end_lat, self.end_lon) < n.path_cost + h(lat2, lon2, self.end_lat, self.end_lon):
                    self.frontier.remove(n)
                    self.append_node(node)
                    print("CHANGE OCCUR!")