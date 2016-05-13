#!/bin/sh

#SBATCH --job-name="fs2k35ibamr"
#SBATCH --output=log_flyingSnake2dRe2000AoA35ds004_ibamr.out
#SBATCH --error=log_flyingSnake2dRe2000AoA35ds004_ibamr.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 16


module load openmpi/1.8/gcc/4.9.2

time mpirun ../../bin/externalFlow2dIBAMR input2d -name flyingSnake2dAoA35ds004
