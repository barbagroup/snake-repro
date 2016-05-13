#!/bin/sh

#SBATCH --job-name="fs2k40Sn16"
#SBATCH --output=log_flyingSnake2k40Stab_n16.out
#SBATCH --error=log_flyingSnake2k40Stab_n16.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 16


MPIRUN=/c1/apps/openmpi/1.8/gcc/4.7/cpu/bin/mpirun
IBAMR_BUILD=/groups/barbalab/src/ibamr/ibamr-objs-openmpi-1.8-gcc-4.7-opt
PROGRAM=$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized

INPUT=input2d
STRUCTURE=flyingSnake2dAoA40ds004

time $MPIRUN $PROGRAM $INPUT --body $STRUCTURE
