import os
import xarray as xr
import kerchunk.hdf
import fsspec
import ujson
import pandas as pd

nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/'
outpath = f'/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'
so = dict(
    anon=True, default_fill_cache=False, default_cache_type='first'
)

df = pd.read_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv').set_index('names')

fs2 = fsspec.filesystem('')

for name in df.index:
    if ((df.loc[name]['NConDISK']==0) & (df.loc[name]['NConOSN']==0)):
        path = nc_path +name + '.nc'
        if(os.path.isfile(path)):
            if(os.path.getsize(path)>10**6):
                with fsspec.open(path, **so) as inf:
                    h5chunks = kerchunk.hdf.SingleHdf5ToZarr(inf, path, inline_threshold=100)
                    outf = outpath + name +'.json'
                    print(outf)
                    with fs2.open(outf, 'wb') as f:
                         f.write(ujson.dumps(h5chunks.translate()).encode());
                df.loc[name]['NConDISK']=1
        else:
            break

df.to_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv')

#folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields'
#arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_Eta-U-V-W-Theta-Salt_f')]





#urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/" + p for p in arr]
#singles = []
#fs2 = fsspec.filesystem('')

#for u in urls:
#    print(u)
#    with fsspec.open(u, **so) as inf:
#        h5chunks = kerchunk.hdf.SingleHdf5ToZarr(inf, u, inline_threshold=100)
        #singles.append(h5chunks.translate())
        ##
        #variable = u.split('/')[-1].split('.')[0]
        #iter = u.split('/')[-1].split('.')[0].split('_')[-1]
#        outpath = f'/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'
#        filename = u.split('/')[-1].split('.')[0] + '.json'
#        outf = outpath + filename #file name to save json to
#        print(outf)
#        with fs2.open(outf, 'wb') as f:
#            f.write(ujson.dumps(h5chunks.translate()).encode());
