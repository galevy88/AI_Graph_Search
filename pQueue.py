

class pQueue:

    def __init__(self):
        self.frontier = []
    
    def append_node(self, node):
        self.frontier.append(node)

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
    
    def find_problematic_child(self, node):
        for n in self.frontier:
            if node.state == n.state:
                if node.path_cost < n.path_cost:
                    self.frontier.remove(n)
                    self.append_node(node)
                    print("CHANGE OCCUR!")