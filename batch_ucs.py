import pandas as pd
from main import batch_find_ucs_rout

def create_df_from_csv():
    df = pd.read_csv('problems.csv')
    return df

def start_batch(df):
    i = 0
    for index, row in df.iterrows():
        source, target, node_path = batch_find_ucs_rout(row[0], row[1])
        print(f"{node_path}")
        print(f"Row Number {i} Finished!")
        i+=1

df = create_df_from_csv()
start_batch(df)