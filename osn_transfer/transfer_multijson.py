import os

import boto3


ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY")
SECRET_KEY=os.environ.get("AWS_SECRET_KEY")

s3 = boto3.resource('s3',
                     aws_access_key_id=ACCESS_KEY,
                     aws_secret_access_key=SECRET_KEY,
                     endpoint_url='https://mghp.osn.xsede.org')

folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json'
arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_Eta-U-V-W-Theta-Salt_f')]
#folder='/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/grid/json_files'
#arr = [filename for filename in os.listdir(folder) if filename.startswith('llc4320_grid_f')]


urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/" + p for p in arr]
#urls = ["/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/grid/json_files/" + p for p in arr]

for u in urls:
    print(u)
    fname = u.split('/')[-1]
    s3.Bucket('cnh-bucket-1').upload_file(u, f"llc_surf/kerchunk_files/{fname}")
