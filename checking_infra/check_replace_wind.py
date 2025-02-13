import os
import pandas as pd
json_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/wind_json/'

df = pd.read_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist_wind.csv').set_index('names')


for name in df.index:
    if (df.loc[name]['JSONonDISK']==1):
        path_json = json_path + name +'.json'
        with open(path_json, 'r') as fp:
                lines = fp.readlines(20)
                for row in lines:
                    #print(row)
                    if row.find("cnh-bucket-1") != -1:
                        df.loc[name]['jsonreplace']=1
df.to_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist_wind.csv')

