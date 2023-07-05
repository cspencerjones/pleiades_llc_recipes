#!/bin/bash

source /etc/profile.d/modules.sh
source /home1/csjone15/.profile

module load singularity

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/osn_transfer/transfer_files.py


singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/osn_transfer/transfer_multijson.py

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/check_for_checksum.py

# -end of script-
