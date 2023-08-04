import os

import boto3

ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY")
SECRET_KEY=os.environ.get("AWS_SECRET_KEY")

s3 = boto3.resource('s3',
                     aws_access_key_id=ACCESS_KEY,
                     aws_secret_access_key=SECRET_KEY,
                     endpoint_url='https://mghp.osn.xsede.org')


folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields'
arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_Eta-U-V-W-Theta-Salt_f')]
#folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/grid/netcdf_files'
#arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_grid')]

urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_fields/" + p for p in arr]
#urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/grid/netcdf_files/" + p for p in arr]

def upload_a_file(u):
    fname = u.split('/')[-1]
    s3.Bucket('cnh-bucket-1').upload_file(u, f"llc_surf/netcdf_files/{fname}")


import sys
sys.path.append(".")
#for u in urls:
#    upload_a_file(u)

from concurrent.futures import ProcessPoolExecutor, as_completed
with ProcessPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(upload_a_file,u) for u in urls]
    results = [f.result() for f in as_completed(futures)]

