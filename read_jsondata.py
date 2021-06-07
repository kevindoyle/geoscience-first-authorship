import pandas as pd
import json
import os


def read_jsons(data_dir, columns=['journal','all_genders', 'all_percent', 'year']):
    """
    read all json files and create a dataframe
    data_dir: path to directory where the json files are located
    columns: these data columns will be kept. The others will be discarded
    """

    dfs = []

    for _, _, files in os.walk(data_dir):
        for file in files:
            with open(os.path.join(data_dir, file)) as f:
                data = json.loads(f.read())
                df = pd.json_normalize(data)
                dropcolumns = [k for k in df.keys() if k not in columns]
                df = df.drop(columns=dropcolumns)
                dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    return (df)