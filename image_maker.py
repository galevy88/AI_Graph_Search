#Gal Levy 208540872
from ways.graph import load_map_from_csv
from ways.draw import plot_path
from main import find_idastar_route
import pandas as pd

def create_df_from_txt():
    df = pd.read_csv('problems_for_ida.txt', sep=",", names=['source', 'end'])
    return df

def start_batch(s, t, func):
    graph = load_map_from_csv()
    source, target, node_path, path_cost = func(s, t)
    plot_path(graph, node_path, source, target)


        
problem = create_df_from_txt()
for i in range(0,10):
    result_df_ucs = start_batch(problem[0], problem[1], find_idastar_route)

