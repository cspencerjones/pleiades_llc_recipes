import os

import boto3

ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY")
SECRET_KEY=os.environ.get("AWS_SECRET_KEY")

s3 = boto3.resource('s3',
                     aws_access_key_id=ACCESS_KEY,
                     aws_secret_access_key=SECRET_KEY,
                     endpoint_url='https://mghp.osn.xsede.org')


path = "/nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/"
for i in range(0,100):
    iterno = 10512+i*144
    print('iterno:',iterno)
    fname = f'surfa_face1_chunkd_{iterno}.json'
    s3.Bucket('cnh-bucket-1').upload_file(path + fname, f"csjones/temp/{fname}")
