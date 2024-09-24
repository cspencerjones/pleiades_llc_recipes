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
#PBS -l select=1:ncpus=2:mpiprocs=1:model=san,pvmem=15gb
#PBS -l walltime=00:20:00
#PBS -j oe
#PBS -W group_list=s2295
#PBS -m e

#s2295 is our group number

module load singularity

# Load a compiler you use to build your executable, for example, comp-intel/2015.0.090.
seq 2 | parallel -j 2 -u \
 "cd $PWD;./job_sing.sh {}"

# -end of script-
