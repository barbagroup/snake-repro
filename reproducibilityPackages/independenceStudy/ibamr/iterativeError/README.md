# Iterative error, Re=2000, AoA=35deg

The present directory contains all input files to compute with IBAMR the flow around a flying-snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000 using different relative tolerances as exit criterion for the velocity and Poisson solvers.

We compute the solution up to 100 non-dimensional time-units in the domain `30cx30c` with the immersed body (with chord-length `c`) centered in it.
The AMR grid  has a grid-spacing of `h=0.004` in the region with highest resolution.

The sub-folder `rtol6` contains all necessary input files to compute the solution using a relative tolerance of `1.0E-06` as exit criterion for each iterative solvers.
To run the simulation:

```
cd rtol6
export IBAMR_PROG=$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized
time mpirun $IBAMR_PROG input2d --body flyingSnake2dAoA35ds004 \
    -stokes_ksp_rtol 1.0E-06 \
    -velocity_ksp_rtol 1.0E-06 \
    -pressure_ksp_rtol 1.0E-06 \
    -cIB_ksp_rtol 1.0E-06
```

where `$IBAMR_BUILD` is your build directory for IBAMR.

The sub-folder `rtol10` contains all necessary input files to compute the solution using a relative tolerance of `1.0E-10` as exit criterion for each iterative solvers.
To run the simulation:

```
cd rtol10
export IBAMR_PROG=$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized
time mpirun $IBAMR_PROG input2d --body flyingSnake2dAoA35ds004 \
    -stokes_ksp_rtol 1.0E-10 \
    -velocity_ksp_rtol 1.0E-10 \
    -pressure_ksp_rtol 1.0E-10 \
    -cIB_ksp_rtol 1.0E-10
```

The Python script `plotForceCoefficientsCompareRTol.py` in the present directory plots the instantaneous force coefficients from the two simulations and calculates the averaged force coefficients between 32 and 64 time-units.

We used the version of IBAMR tagged [`snake-repro`](https://github.com/mesnardo/IBAMR/releases/tag/snake-repro), the linear algebra library [`PETSc-3.5.2`](https://www.mcs.anl.gov/petsc/download/index.html), `OpenMPI-1.8`, `gcc-4.7.0`, `SAMRAI-2.4.4`, `HDF5-1.8.13`, and `SILO-4.10`.

For the simulation `rtol6`, we computed about 100 time-units of flow-simulation on 16 CPU cores (1 compute node) in 48 hours.
For the simulation `rtol10`, we computed 100 time-units of flow-simulation on 16 CPU cores (1 compute nodes) in about 68 hours.
