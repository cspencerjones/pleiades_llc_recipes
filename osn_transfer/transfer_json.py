import os

import boto3

ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY")
SECRET_KEY=os.environ.get("AWS_SECRET_KEY")

s3 = boto3.resource('s3',
                     aws_access_key_id=ACCESS_KEY,
                     aws_secret_access_key=SECRET_KEY,
                     endpoint_url='https://mghp.osn.xsede.org')


path = "/nobackup/csjone15/pleiades_llc_recipes/osn_transfer/"
fname = f'replaced_fields.json'
s3.Bucket('cnh-bucket-1').upload_file(path + fname, f"csjones/temp/{fname}")
