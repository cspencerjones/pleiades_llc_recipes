#!/bin/bash

source /etc/profile.d/modules.sh
source /home1/csjone15/.profile

csv_file="/nobackup/csjone15/pleiades_llc_recipes/checking_infra/checklist_wind.csv"

pattern_found=false

# Read the CSV file line by line
while IFS= read -r line; do
    # Extract the values from the line
    values=$(echo "$line" | cut -d',' -f2-)
    # Check if the values are "0,0,0,0"
    if [ "$values" == "1,1,1,0,0" ]; then
        pattern_found=true
	break
    fi
done < "$csv_file"
echo "Found iterno $ts for the first line with 0,0,0,0,0: $line"

if [ "$pattern_found" = false ]; then
    echo "Pattern not found in any line. Exiting..."
    exit 1
fi


module load singularity

echo message | date

#singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pangeo.sif python /nobackup/csjone15/pleiades_llc_recipes/osn_transfer/transfer_files.py

echo message | date

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pangeo.sif python /nobackup/csjone15/pleiades_llc_recipes/osn_transfer/transfer_multijson_wind.py

echo message | date

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/check_wind_checksum.py

echo message | date

# -end of script-
