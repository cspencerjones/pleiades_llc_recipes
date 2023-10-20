print('begin garbage disposal')
import pandas as pd
import os

df = pd.read_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist_wind.csv').set_index('names')

json_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/wind_json/'

nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_wind/'

for name in df.index:
    print(name)
    if ((df.loc[name]['JSONonDISK']==1) & (df.loc[name]['JSONonOSN']==1)):
        try:
          os.remove(json_path + name + '.json')
        except OSError as e: # name the Exception `e`
          print("Failed with:", e.strerror) # look what it says
          print("Error code:", e.code)
        df.loc[name]['JSONonDISK']=0
        if ((df.loc[name]['NConDISK']==1) & (df.loc[name]['NConOSN']==1)):
            try: 
              os.remove(nc_path + name + '.nc')
              print("tried removing", nc_path + name + '.nc')
            except OSError as e: # name the Exception `e`
              print("Failed with:", e.strerror) # look what it says
              print("Error code:", e.code)
            df.loc[name]['NConDISK']=0

df.to_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist_wind.csv')
