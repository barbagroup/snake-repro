#!/bin/sh

#SBATCH --job-name="fs1k30n32bcgs"
#SBATCH --output=log_summary_fs1k30n32bcgs_%j.out
#SBATCH --error=log_summary_fs1k30n32bcgs_%j.err
#SBATCH --partition=short
#SBATCH --time=48:00:00
#SBATCH -n 32

OPENMPI_DIR=/c1/apps/openmpi/1.8/gcc/4.9.2
MPIRUN=$OPENMPI_DIR/bin/mpirun

PETIBM_BUILD=$HOME/src/petibm/petibm-0.1_petsc-3.5.2_openmpi-1.8_gcc-4.9.2_opt
PETIBM2D=$PETIBM_BUILD/bin/petibm2d

time $MPIRUN $PETIBM2D -caseFolder $PWD \
	-sys2_ksp_type bcgs \
	-sys2_pc_type gamg \
	-sys2_pc_gamg_type agg \
	-sys2_pc_gamg_agg_nsmooths 1 \
	-log_summary
