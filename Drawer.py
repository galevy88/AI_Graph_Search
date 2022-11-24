#Gal Levy 208540872
import pandas as pd
import matplotlib.pyplot as plt
from ways.tools import compute_distance
from Node_Functions import get_lat_lon

def parser(direction, str):
    
    str = str[1:-1]
    if len(str) <= 7:
        return int(str)
    junction = ""
    if direction == 'start':
        for s in str:
            if s != ',':
                junction += s
            else:
                return int(junction)
    if direction == 'end':
        i = len(str) - 1
        while str[i] != ' ':
            junction += str[i]
            i-=1
        i = len(junction) - 1
        final_junction = ""
        while i >= 0:
            final_junction += junction[i]
            i-=1

        return int(final_junction)




def create_df_from_csv():
    df_astar = pd.read_csv('results\\AStarRuns.txt', sep=" - ", names=["path", "path cost"], engine='python')
    return  df_astar

def draw_plot(ucs_costs, astar_costs):
    plt.scatter(ucs_costs, astar_costs)
    plt.xlabel("Huristic costs")
    plt.ylabel("AStar costs")
    plt.show()

def create_huristic_costs(astar_path):
    ls = []
    for index, row in astar_path.iterrows():
        source = parser('start', row[0])
        target = parser('end', row[0])       
        lat1, lon1 = get_lat_lon(source)
        lat2, lon2 = get_lat_lon(target)
        distance = compute_distance(lat1, lon1, lat2, lon2) / 110
        print(f"SOURCE: {source} TARGET: {target} DISTANCE: {distance}")
        ls.append(distance)
    return ls
        

df_astar = create_df_from_csv()
astar_costs = df_astar.iloc[:,-1:]
astar_path = df_astar.iloc[:,0:1]
huristic_costs = create_huristic_costs(astar_path)
draw_plot(huristic_costs, astar_costs)