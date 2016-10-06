# Grid independence, Re=2000, AoA=35deg

The present directory contains all input files to compute with PetIBM the flow around a flying-snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000 on different grids.

We compute 80 non-dimensional time-units on a 2D structured stretched Cartesian grid that covers a `30cx30c` domain with the immersed boundary 
(with chord-length `c`) centered in it.
The spatial discretization is uniform in the region `[-0.52, 3.48]x[-2.0, 2.0]` and we test two different grid-spacings: `h=0.004` and `h=0.006`.
Outside, the gridlines are stretched with constant ratio `1.01` in all directions.
For each grid, we compute `200k` time-steps with time-increment `0.0004`.
The exit criterion for the velocity and Poisson solver is set with an absolute tolerance of `1.0E-05`.

The sub-folder `h0.004` contains all necessary input files to compute the numerical solution on the fine grid.
To run the simulation:

    time mpirun $PETIBM2D -directory h0.004 -log_summary

where `$PETIBM2D` is the path to the PetIBM executable for 2D simulations.

The sub-folder `h0.006` contains all necessary input files to compute the numerical solution on the coarse grid.
To run the simulation:

    time mpirun $PETIBM2D -directory h0.006 -log_summary


The Python script `plotForceCoefficientsCompareMeshes.py` in the present directory plots the instantaneous force coefficients from the two simulations and calculates the averaged force coefficients between 32 and 64 time-units.

We used [`PetIBM-0.1.1`](https://github.com/barbagroup/PetIBM/releases/tag/0.1.1), the linear algebra library [`PETSc-3.5.2`](https://www.mcs.anl.gov/petsc/download/index.html), and `openmpi-1.8`.

For the simulation `h0.004`, we computed 80 time-units of flow-simulation on 32 CPU cores (2 compute nodes) in about 38 hours.
For the simulation `h0.006`, we computed 80 time-units of flow-simulation on 16 CPU cores (1 compute node) in about 38 hours.
