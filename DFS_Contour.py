#Gal Levy 208540872
from distance_functions import cost_function, huristic_function
from Node_Functions import get_lat_lon
import math

def f(node, end):
    lat1, lon1 = get_lat_lon(node.state)
    lat2, lon2 = get_lat_lon(end)
    fCost = node.path_cost + huristic_function(lat1, lon1, lat2, lon2)
    return fCost

def DFS_Countur(node, end, limit):
    if f(node, end) > limit: return -1, f(node, end)
    if node.state == end: return node, limit
    #print(f"node.state: {node.state} end: {end}")
    nextF = math.inf
    for child in node.expand(cost_function):
        solution, newf = DFS_Countur(child, end, limit)
        if solution != -1: return solution, limit
    nextF = min(nextF, newf)
    
    return -1, nextF



















    # nextf = 1
    # while frontier.isNotEmpty():
    #     current_node = frontier.pop()
    #     for child in current_node.expand(cost_function):
    #         solution_node, newf = DFS_Countur(child, end, flimit)
    #     if solution_node != -1: return solution_node, flimit
    #     nextf = min(nextf, newf)

    # return -1, nextf    
