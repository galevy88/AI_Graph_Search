import pandas as pd
from main import batch_find_ucs_rout


def convert_problem_list_to_csv(df):
    df.to_csv('results\\UCSRuns.csv', index = False, header=True)


def create_df_from_csv():
    df = pd.read_csv('problems.csv')
    return df

def start_batch(df):
    i = 0
    dfList = []
    for index, row in df.iterrows():
        source, target, node_path, path_cost = batch_find_ucs_rout(row[0], row[1])
        print(f"#{i}# SOURCE: {source} TARGET: {target} PATH: {node_path} Row Number {i} Finished!")
        i+=1
        dfList.append([source, target, node_path, path_cost])
    df = pd.DataFrame(dfList, columns=['source','target','path', 'path cost'])
    print(df)
    return df

problem = create_df_from_csv()
result_df = start_batch(problem)
convert_problem_list_to_csv(result_df)