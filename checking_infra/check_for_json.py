import os
import pandas as pd
json_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'

df = pd.read_csv('checklist1.csv').set_index('names')


for name in df.index:
    if (df.loc[name]['NConDISK']==1):
        path = json_path +name + '.json'
        if(os.path.isfile(path)):
                df.loc[name]['JSONonDISK']=1

df.to_csv('checklist1.csv')

