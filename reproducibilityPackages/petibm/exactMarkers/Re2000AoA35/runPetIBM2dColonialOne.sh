#!/bin/sh

# file: runPetIBM2dColonialOne.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# brief: Runs PetIBM on a 2d problem on Colonial One.


#SBATCH --job-name="2k35petibm"
#SBATCH --output=log%j.out
#SBATCH --error=log%j.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 32


module load gcc/4.9.2
module load openmpi/1.8/gcc/4.9.2


PETIBM_BUILD="/groups/barbalab/mesnardo/build/petibm-0.1.1-petsc-3.5.2-openmpi-1.8-gcc-4.9.2"
PETIBM2D="$PETIBM_BUILD/bin/petibm2d"

time mpirun $PETIBM2D -directory $PWD -log_summary
