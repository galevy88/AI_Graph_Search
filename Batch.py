import pandas as pd
from main import find_ucs_rout
from main import find_astar_route


def convert_problem_list_to_txt(df, location):
    with open(f'{location}.txt', 'w') as f:
        for index, row in df.iterrows():
            f.write(f"{row['source']}; {row['target']}; {row['path']}; {row['path cost']}\n")


def create_df_from_txt():
    df = pd.read_csv('problems.txt', sep=",", names=['source', 'end'])
    return df

def start_batch(df, func):
    i = 0
    dfList = []
    for index, row in df.iterrows():
        source, target, node_path, path_cost = func(row[0], row[1])
        print(f"#{i}# SOURCE: {source} TARGET: {target} PATH: {node_path} Row Number {i} Finished!")
        i+=1
        dfList.append([source, target, node_path, path_cost])
    df = pd.DataFrame(dfList, columns=['source','target','path', 'path cost'])
    print(df)
    return df

problem = create_df_from_txt()
result_df_ucs = start_batch(problem, find_ucs_rout)
result_df_astar = start_batch(problem, find_astar_route)
convert_problem_list_to_txt(result_df_ucs, 'results\\UCSRuns')
convert_problem_list_to_txt(result_df_astar, 'results\\AStarRuns')