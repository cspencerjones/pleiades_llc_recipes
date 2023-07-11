#PBS -S /bin/csh
#PBS -N cfd
# This example uses the Sandy Bridge nodes
# User job can access ~31 GB of memory per Sandy Bridge node.
# A memory intensive job that needs more than ~1.9 GB
# per process should use less than 16 cores per node
# to allow more memory per MPI process. This example
# asks for 32 nodes and 8 MPI processes per node.
# This request implies 32x8 = 256 MPI processes for the job.
#PBS -q normal
#PBS -l select=1:ncpus=5:mpiprocs=1:mem=30GB:model=san,pmem=3gb
#PBS -l walltime=01:00:00
#PBS -j oe
#PBS -W group_list=s2295
#PBS -m e

#s2295 is our group number


module load singularity

echo message | date

# Load a compiler you use to build your executable, for example, comp-intel/2015.0.090.
seq 111 119 | parallel -j 5 -u \
 "cd $PWD;./job_sing.sh {}"

echo message | date

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/make_kerch.py

echo message | date

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/check_for_json.py

echo message | date

find /nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/surf_extract/surf_json/ -type f -wholename '*' | xargs -P10 sed -i 's/\\\/nobackup\\\/csjone15\\\/pleiades_llc_recipes\\\/python_cli_data_export\\\/surf_extract\\\/surf_fields/cnh-bucket-1\\\/llc_surf\\\/netcdf_files/g'


singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 /nobackup/csjone15/notebook_pang python /nobackup/csjone15/pleiades_llc_recipes/checking_infra/check_replace.py


# I removed --memfree 1GB
# -end of script-
