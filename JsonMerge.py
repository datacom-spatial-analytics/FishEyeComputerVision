import pandas as pd
import glob, os, json
import numpy as np

json_dir = './images'

json_pattern = os.path.join(json_dir, '*.json')
file_list = glob.glob(json_pattern)

dfs = []
for file in file_list:
    with open(file) as f:
        json_data = pd.json_normalize(json.loads(f.read()))
        json_data['Date/Time'] = file.rsplit("/", 1)[-1]
    dfs.append(json_data)
df = pd.concat(dfs)