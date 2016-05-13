#!/bin/sh

# file: runCuIBMColonialOne.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# brief: Runs cuIBM on Colonial One.


#SBATCH --job-name="2k35c051"
#SBATCH --output=log%j.out
#SBATCH --error=log%j.err
#SBATCH --partition=gpu
#SBATCH --time=48:00:00
#SBATCH -n 1


module load gcc/4.9.2
module load cuda/toolkit/7.5

CUIBM="/home/mesnardo/bin/cuibm-production-cusp-0.5.1"

time $CUIBM -caseFolder $PWD
