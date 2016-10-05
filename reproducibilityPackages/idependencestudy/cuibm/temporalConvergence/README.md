# Temporal convergence, Re=2000, AoA=35deg, h=0.00267

The present directory contains all input files to evaluate the temporal error.

We compare the solution after `0.15` time-units of flow-simulation on the finest mesh (`h=0.00267`) with various time-increments: `5.0E-05`, `1.0E-04`, and `2.0E-04`.

We fix to exit criterion of the velocity solver with an absolute tolerance of `1.0E-16` and the one of the Poisson solver with an absolute tolerance of `1.0E-11` (based on the estimation of the iterative errors done in the folder `cuibm/iterativeConvergence`).

The solution is computed on a 2D structured stretched Cartesian grid that covers a `30cx30c` domain with the immersed boundary 
(with chord-length `c`) centered in it.
The spatial discretization is uniform in the region `[-0.51966, 3.48]x[-1.99983, 1.99983]` with grid-spacing `0.00267`.
Outside, the gridlines are stretched with constant ratio `1.01` in all directions.

To avoid the transient regime due to the impulsively start, we use the solution after `0.1` time-units obtained using an absolute tolerance of `1.0E-16` for the Poisson solver and obtained during the iterative convergence study (simulation directory: `../iterativeConvergence/atol16`).
We then compute an extra `0.05` time-unit and compare the solution obtained with each time-increment.

```
cp -r ../iterativeConvergence/atol16/0001000 dt5.0E-05
cp -r ../iterativeConvergence/atol16/0001000 dt1.0E-04
cp -r ../iterativeConvergence/atol16/0001000 dt2.0E-04
time $CUIBM -caseFolder dt5.0E-05
time $CUIBM -caseFolder dt1.0E-04
time $CUIBM -caseFolder dt2.0E-04
```

where `$CUIBM` is the path to the cuIBM executable.

At `0.15` time-unit of flow-simulation, we compare the differences in the forces, the flux fields, and the pressure fields from each run with the machine-accurate solution.
The is done with the Python script `getTemporalConvergence.py`.

We used the version of cuIBM tagged [`snake-repro-cusp-0.5.1`](https://github.com/barbagroup/cuIBM/releases/tag/snake-repro-cusp-0.5.1), the linear algebra library [`CUSP-0.5.1`](https://github.com/cusplibrary/cusplibrary/releases/tag/v0.5.1), and `CUDA-7.5`.

Each run requires about 6GB of memory on the GPU device.
We used a GPU K40 to compute the solutions.