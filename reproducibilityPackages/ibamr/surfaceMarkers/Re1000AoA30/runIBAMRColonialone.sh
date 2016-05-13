#!/bin/sh

#SBATCH --job-name="fs1k30ibamr"
#SBATCH --output=log_flyingSnake2dRe1000AoA30ds004_ibamr.out
#SBATCH --error=log_flyingSnake2dRe1000AoA30ds004_ibamr.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 16


module load openmpi/1.8/gcc/4.9.2

time mpirun ../../bin/externalFlow2dIBAMR input2d -name flyingSnake2dAoA30ds004
