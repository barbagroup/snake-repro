# Grid convergence, Re=2000, AoA=35deg

The present directory contains all input files to assess grid-convergence in the numerical solution.

We compute about `6` time-units of flow-simulation on three systematically refined grids.
The domain consists in a `30cx30c` square with the immersed boundary 
(with chord-length `c`) centered in it.
The coarse grid has a grid-spacing of `h=0.006` in the uniform region; outside this region the gridlines are stretched to the domain boundaries with a constant ratio of 1.01 in all directions.
The medium and fine grids have a grid-spacing of `h=0.004` and `h=0.006`, respectively, in the uniform region; the same stretching ratio of `1.01` is used.
We end up with a refinement ratio of `1.5 (=0.006/0.004=0.004/0.00267)`.

We choose a time-increment of `0.0002` and set the exit criterion for the velocity and Poisson solvers with an absolute tolerance of `1.0E-16` and `1.0E-08`, respectively.

To run the simulations:

```
time $CUIBM -caseFolder h0.006
time $CUIBM -caseFolder h0.004
time $CUIBM -caseFolder h0.00267
```

where `$CUIBM` is the path to the cuIBM executable.

We used the version of cuIBM tagged [`snake-repro-cusp-0.5.1`](https://github.com/barbagroup/cuIBM/releases/tag/snake-repro-cusp-0.5.1), the linear algebra library [`CUSP-0.5.1`](https://github.com/cusplibrary/cusplibrary/releases/tag/v0.5.1), and `CUDA-7.5`.

The simulation on the fine grid requires about 6 GB of memory on the GPU device; we used a GPU K40 to compute the solution.

The simulation on the medium grid requires about 3 GB of memory on the GPU device; we used a GPU K20 to compute the solution.

The simulation on the coarse grid requires about 1.8 GB of memory on the GPU device; we used a GPU K20 to compute the solution.