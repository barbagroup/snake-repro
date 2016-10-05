# Grid independence, Re=2000, AoA=35deg

The present directory contains all input files to compute with IBAMR the flow around a flying-snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000 using two different minimal grid-spacings for the AMR grid: h=0.004 (the one reported in our manuscript) and h=0.002.

We compute the solution up to 100 non-dimensional time-units in the domain `30cx30c` with the immersed body (with chord-length `c`) centered in it.

The sub-folder `h0.004` contains all necessary input files to compute the solution on a AMR grid where the smallest grid-spacing is h=0.004.
To run the simulation:

```
cd 0.004
export IBAMR_PROG=$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized
time mpirun $IBAMR_PROG input2d --body flyingSnake2dAoA35ds004
```

where `$IBAMR_BUILD` is your build directory for IBAMR.

The sub-folder `h0.002` contains all necessary input files to compute the solution on a AMR grid where the smallest grid-spacing is h=0.002.
To run the simulation:

```
cd h0.002
export IBAMR_PROG=$IBAMR_BUILD/examples/ConstraintIB/externalFlowBluffBody2dStabilized/externalFlowBluffBody2dStabilized
time mpirun $IBAMR_PROG input2d --body flyingSnake2dAoA35ds002
```

The Python script `plotForceCoefficientsCompareMeshes.py` in the present directory plots the instantaneous force coefficients from the two simulations and calculates the averaged force coefficients between 32 and 64 time-units.

We used the version of IBAMR tagged [`snake-repro`](https://github.com/mesnardo/IBAMR/releases/tag/snake-repro), the linear algebra library [`PETSc-3.5.2`](https://www.mcs.anl.gov/petsc/download/index.html), `OpenMPI-1.8`, `gcc-4.7.0`, `SAMRAI-2.4.4`, `HDF5-1.8.13`, and `SILO-4.10`.

For the simulation `h0.004`, we computed around 100 time-units of flow-simulation on 16 CPU cores (1 compute node) in 48 hours.
For the simulation `h0.002`, we computed around 66 time-units of flow-simulation on 16 CPU cores (1 compute nodes) in about 166 hours.
