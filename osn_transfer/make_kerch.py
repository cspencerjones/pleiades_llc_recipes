import os
folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields'
arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_Eta-U-V-W-Theta-Salt_f1_k0_chunkd_iter')]


import xarray as xr
import kerchunk.hdf
import fsspec
import ujson



urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/" + p for p in arr]
so = dict(
    anon=True, default_fill_cache=False, default_cache_type='first'
)
singles = []
fs2 = fsspec.filesystem('')

for u in urls:
    print(u)
    with fsspec.open(u, **so) as inf:
        h5chunks = kerchunk.hdf.SingleHdf5ToZarr(inf, u, inline_threshold=100)
        #singles.append(h5chunks.translate())
        ##
        #variable = u.split('/')[-1].split('.')[0]
        iter = u.split('/')[-1].split('.')[0].split('_')[-1]
        outf = f'/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/surfa_face1_chunkd_{iter}.json' #file name to save json to
        with fs2.open(outf, 'wb') as f:
            f.write(ujson.dumps(h5chunks.translate()).encode());
