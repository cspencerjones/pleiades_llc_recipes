import hashlib
import s3fs
import pandas as pd
import os

def etag_checksum(filename, chunk_size=8 * 1024 * 1024):
    md5s = []
    with open(filename, 'rb') as f:
        for data in iter(lambda: f.read(chunk_size), b''):
            md5s.append(hashlib.md5(data).digest())
    m = hashlib.md5(b"".join(md5s))
    return '{}-{}'.format(m.hexdigest(), len(md5s))

def md5_checksum(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        for data in iter(lambda: f.read(1024 * 1024), b''):
            m.update(data)
    return m.hexdigest()

nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/'

endpoint_url = 'https://mghp.osn.xsede.org'
fs = s3fs.S3FileSystem(
    anon=True,
    client_kwargs={'endpoint_url': endpoint_url}
)


df = pd.read_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv').set_index('names')

for name in df.index:
    if ((df.loc[name]['NConDISK']==1) & (df.loc[name]['NConOSN']==0)):
        check1 = etag_checksum(nc_path + name + '.nc')
        file_url = 'cnh-bucket-1/llc_surf/netcdf_files/' + name +'.nc'
        to_check = fs.info(file_url)['ETag'].strip('\"')
#        if (check1==to_check):
#            df.loc[name]['NConOSN']=1

#nc_path = '/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/'

endpoint_url = 'https://mghp.osn.xsede.org'
fs = s3fs.S3FileSystem(
    anon=True,
    client_kwargs={'endpoint_url': endpoint_url}
)


for name in df.index:
    if (df.loc[name]['JSONonDISK']==1):
        check1 = md5_checksum(nc_path + name + '.json')
        file_url = 'cnh-bucket-1/llc_surf/kerchunk_files/' + name +'.json'
        to_check = fs.info(file_url)['ETag'].strip('\"')
#        if (check1==to_check):
#            df.loc[name]['JSONonOSN']=1

df.to_csv('/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist1.csv')
