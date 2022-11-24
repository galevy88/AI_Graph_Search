#Gal Levy 208540872
'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from ways.graph import load_map_from_csv
import stat_functions as Functions


def map_statistics(roads):
    number_of_junctions = len(roads)
    number_of_links = Functions.calculate_number_of_links(roads)
    branching_factor = Functions.calculate_branching_factor(roads,number_of_junctions, number_of_links)
    link_distance = Functions.calculate_links_distance(roads, number_of_links)
    histogram = Functions.calculate_histogram(roads)
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    return {
        'Number of junctions' : number_of_junctions,
        'Number of links' : number_of_links,
        'Outgoing branching factor' : branching_factor,
        'Link distance' : link_distance,
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram' : histogram,  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()

