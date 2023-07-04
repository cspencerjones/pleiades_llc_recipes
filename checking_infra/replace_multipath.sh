#PBS -S /bin/csh
#PBS -N cfd
# per process should use less than 16 cores per node
# to allow more memory per MPI process. This example
# asks for 32 nodes and 8 MPI processes per node.
# This request implies 32x8 = 256 MPI processes for the job.
#PBS -q devel
#PBS -l select=1:ncpus=10:model=ivy
#PBS -l walltime=00:20:00
#PBS -j oe
#PBS -W group_list=s2295
#PBS -m e

find /nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/ -type f -wholename '*' | xargs -P10 sed -i 's/\\\/nobackup\\\/csjone15\\\/pleiades_llc_recipes\\\/python_cli_data_export\\\/surf_extract\\\/surf_fields/cnh-bucket-1\\\/llc_surf\\\/netcdf_files/g'

module load singularity

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/check_replace.py 
