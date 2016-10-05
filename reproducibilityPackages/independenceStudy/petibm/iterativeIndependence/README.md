# Iterative independence, Re=2000, AoA=35deg, h=0.004

The present directory contains all input files to compute with PetIBM the flow around a flying-snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000 using different relative tolerances as exit criterion for the velocity and Poisson solvers.

We compute about 80 non-dimensional time-units on a 2D structured stretched Cartesian grid that covers a `30cx30c` domain with the immersed boundary 
(with chord-length `c`) centered in it.
The spatial discretization is uniform in the region `[-0.52, 3.48]x[-2.0, 2.0]` with grid-spacing `0.004`.
Outside, the gridlines are stretched with constant ratio `1.01` in all directions.
The time-increment is set to `4.0E-04`  and we compute `200k` time-steps.

The sub-folder `rtol5` contains all necessary input files to compute the solution using a relative tolerance of `1.0E-05` as exit criterion for the velocity and Poisson solvers.
To run the simulation:

    time mpirun $PETIBM2D -directory rtol5 -log_summary

where `$PETIBM2D` is the path to the PetIBM executable for 2D simulations.

The sub-folder `rtol8` contains all necessary input files to compute the solution using a relative tolerance of `1.0E-08` as exit criterion for the velocity and Poisson solvers.
To run the simulation:

    time mpirun $PETIBM2D -directory rtol8 -log_summary

The Python script `plotForceCoefficientsCompareRTol.py` in the present directory plots the instantaneous force coefficients from the two simulations and calculates the averaged force coefficients between 32 and 64 time-units.

We used [`PetIBM-0.1.1`](https://github.com/barbagroup/PetIBM/releases/tag/0.1.1), the linear algebra library [`PETSc-3.5.2`](https://www.mcs.anl.gov/petsc/download/index.html), and `openmpi-1.8`.

For the simulation `rtol5`, we computed 80 time-units of flow-simulation on 32 CPU cores (2 compute nodes) in about 38 hours.
For the simulation `rtol8`, we computed  around 74 time-units of flow-simulation on 32 CPU cores (2 compute nodes) over 9 days and 12 hours.
