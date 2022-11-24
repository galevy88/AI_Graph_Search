#Gal Levy 208540872

from Node import Node
from DFS_Contour import DFS_Countur

def IDA(start, end):
    start_node = Node(start, [], 0)
    limit = 0
    while(True):
        solution_node, limit = DFS_Countur(start_node, end, limit)
        if solution_node != -1:
            return solution_node
        if limit > 1:
            return -1
