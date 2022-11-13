
import math
from collections import namedtuple
from collections import Counter



def calculate_histogram(roads):
    list_of_highway_types = []
    for i in range(0, len(roads)):
        for j in range(0, len(roads[i].links)):
            highway_type = roads[i].links[j].highway_type
            list_of_highway_types.append(highway_type)
    histogram = Counter(list_of_highway_types)
    return histogram

def calculate_links_distance(roads, number_of_links):
    total_distance = 0
    high_d = 0
    low_d = math.inf
    avg_d = 0
    for i in range(0, len(roads)):
        for j in range(0, len(roads[i].links)):
            distance = roads[i].links[j].distance
            if distance > high_d:
                high_d = distance
            if distance < low_d:
                low_d = distance
            total_distance += roads[i].links[j].distance
    avg_d = float(total_distance / number_of_links)
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    stat = Stat(max=high_d, min=low_d, avg=avg_d)
    return stat

def calculate_branching_factor(roads,number_of_junctions, number_of_links):
    high_bf = 0
    low_bf = math.inf
    avg_bf = 0
    for i in range(0, len(roads)):
        bf = len(roads[i].links)
        if bf > high_bf:
            high_bf = bf
        if bf < low_bf:
            low_bf = bf
    avg_bf = float(number_of_links / number_of_junctions)
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    stat = Stat(max=high_bf, min=low_bf, avg=avg_bf)
    return stat

def calculate_number_of_links(roads):
    total_links = 0
    for i in range(0, len(roads)):
        total_links += len(roads[i].links)
    return total_links