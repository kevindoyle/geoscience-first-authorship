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

    # clean some journal names

    df.loc[df.journal=='E%26PSL','journal'] = 'EPSL'

    df.loc[df.journal.str.contains("Bulletin"),'journal'] = 'BSSA'

    df.loc[df.journal.str.contains("Seismological"),'journal'] = 'SRL'

    # Remove rows for papers from 2021
    df = df[~df['year'].isin(['2021'])].copy()

    # add IF
    dict_IF = {'Nature': 46.486, 'Science': 41.845, 'NatureGeoscience': 16.103, 'EPSL': 4.823, 'GRL': 4.952, 
        'JGRSolidEarth': 4.191, 'G3': 3.721, 'SRL': 3.131, 'Tectp': 3.048, 'SolidEarth': 2.921, 
       'GEOPHYSICS': 3.093, 'GJI': 2.834, 'BSSA': 2.274, 'PEPI': 2.413}

    df['IF'] = df['journal'].map(dict_IF)
    return (df)    