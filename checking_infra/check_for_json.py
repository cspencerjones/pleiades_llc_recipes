import os
import pandas as pd
nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/'
json_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'

df = pd.read_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv').set_index('names')


for name in df.index:
    if ((df.loc[name]['NConDISK']==0) & (df.loc[name]['NConOSN']==0)):
        path = nc_path +name + '.nc'
        if(os.path.isfile(path)):
            if(os.path.getsize(path)>10**6):
                df.loc[name]['NConDISK']=1
    if (df.loc[name]['NConDISK']==1):
        path = json_path +name + '.json'
        if(os.path.isfile(path)):
                df.loc[name]['JSONonDISK']=1

df.to_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv')

