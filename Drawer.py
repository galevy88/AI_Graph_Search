
import pandas as pd
import matplotlib.pyplot as plt
from ways.tools import compute_distance
from Node_Functions import get_lat_lon

def create_df_from_csv():
    df_astar = pd.read_csv('results\\AStarRuns.txt', sep=";", names=['source', 'target', "path", "path cost"])
    return  df_astar

def draw_plot(ucs_costs, astar_costs):
    plt.scatter(ucs_costs, astar_costs)
    plt.xlabel("Hutistic costs")
    plt.ylabel("AStar costs")
    plt.show()

def create_huristic_costs(df_aster):
    ls = []
    for index, row in df_astar.iterrows():
        source = row[0]
        target = row[1]
        lat1, lon1 = get_lat_lon(source)
        lat2, lon2 = get_lat_lon(target)
        distance = compute_distance(lat1, lon1, lat2, lon2) / 110
        print(f"SOURCE: {source} TARGET: {target} DISTANCE: {distance}")
        ls.append(distance)
    return ls
        

df_astar = create_df_from_csv()
astar_costs = df_astar.iloc[:,-1:]
huristic_costs = create_huristic_costs(create_df_from_csv)
draw_plot(huristic_costs, astar_costs)