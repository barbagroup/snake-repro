#!/bin/sh

# file: runPetIBM2dColonialOne.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# brief: Runs PetIBM on a 2d problem on Colonial One.


#SBATCH --job-name="bugFix"
#SBATCH --output=log%j.out
#SBATCH --error=log%j.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 32


OPENMPI_DIR="/c1/apps/openmpi/1.8/gcc/4.9.2"
MPIRUN="$OPENMPI_DIR/bin/mpirun"

PETIBM_BUILD="$HOME/builds/petibm-0.1_develop_bugFixPoisson_petsc-3.5.2_openmpi-1.8_gcc-4.9.2"
PETIBM2D="$PETIBM_BUILD/bin/petibm2d"

time $MPIRUN $PETIBM2D -directory $PWD -log_summary
