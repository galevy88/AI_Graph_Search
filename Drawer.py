
import pandas as pd
import matplotlib.pyplot as plt

def create_df_from_csv():
    df_ucs = pd.read_csv('results\\UCSRuns.csv')
    df_astar = pd.read_csv('results\\AStarRuns.csv')
    return df_ucs, df_astar

def draw_plot(ucs_costs, astar_costs):
    plt.scatter(ucs_costs, astar_costs)
    plt.xlabel("UCS")
    plt.ylabel("AStar")
    plt.show()

df_ucs, df_astar = create_df_from_csv()
ucs_costs = df_ucs.iloc[:,-1:]
astar_costs = df_astar.iloc[:,-1:]
draw_plot(ucs_costs, astar_costs)