#Gal Levy 208540872
import pandas as pd
from main import find_ucs_rout
from main import find_astar_route
from main import find_idastar_route
import time

def create_df_from_txt():
    df = pd.read_csv('problems_for_ida.txt', sep=",", names=['source', 'end'])
    return df

def evaluate_runtime(problem):
    runtime_ucs = []
    runtime_astar = []
    runtime_idastar = []
    i = 1
    for index, row in problem.iterrows():
        start = time.time()
        source, target, node_path, path_cost = find_ucs_rout(row[0], row[1])
        end = time.time()
        runtime_ucs.append(end -start)
        print(f"#{i}# Time UCS for  : {row[0]} -> {row[1]} is {end - start}")
        start = 0
        end = 0

        start = time.time()
        source, target, node_path, path_cost = find_astar_route(row[0], row[1])
        end = time.time()
        runtime_astar.append(end -start)
        print(f"#{i}# Time A* for   : {row[0]} -> {row[1]} is {end - start}")
        start = 0
        end = 0
    
        start = time.time()
        source, target, node_path, path_cost = find_idastar_route(row[0], row[1])
        end = time.time()
        runtime_idastar.append(end -start)
        print(f"#{i}# Time IDA* for : {row[0]} -> {row[1]} is {end - start}")
        start = 0
        end = 0
        i+=1
    
    print("\n")
    print(f"Run time UCS  : {runtime_ucs}")
    print(f"Run time A*   : {runtime_astar}")
    print(f"Run time IDA* : {runtime_idastar}")

    summation_ucs = sum(runtime_ucs)
    summation_astar = sum(runtime_astar)
    summation_idastar = sum(runtime_idastar)

    print("\n")
    print(f"Summation UCS  : {summation_ucs}")
    print(f"Summation A*   : {summation_astar}")
    print(f"Summation IDA* : {summation_idastar}")

    avarage_ucs = summation_ucs / 10
    avarage_astar = summation_astar / 10
    avarage_idastar = summation_idastar / 10

    print("\n")
    print(f"Avarage UCS  : {avarage_ucs}")
    print(f"Avarage A*   : {avarage_astar}")
    print(f"Avarage IDA* : {avarage_idastar}")
    
    
problem = create_df_from_txt()
evaluate_runtime(problem)