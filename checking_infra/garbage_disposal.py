print('begin garbage disposal')
import pandas as pd
import os

df = pd.read_csv('checklist1.csv').set_index('names')

json_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'

nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/'

for name in df.index:
    print(name)
    if ((df.loc[name]['JSONonDISK']==1) & (df.loc[name]['JSONonOSN']==1)):
        os.remove(json_path + name + '.json')
        df.loc[name]['JSONonDISK']=0
        if ((df.loc[name]['NConDISK']==1) & (df.loc[name]['NConOSN']==1)):
            os.remove(nc_path + name + '.nc')
            df.loc[name]['NConDISK']=0

df.to_csv('checklist1.csv')
