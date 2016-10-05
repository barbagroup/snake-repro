# Iterative errors, Re=2000, AoA=35deg, h=0.00267

The present directory contains all input files to estimate the iterative errors versus the absolute tolerance of the Poisson solver.

To evaluate the iterative error, we compute the solution on the finest mesh (`h=0.00267`) over a small number of time-steps with time-increment `0.0001`.
We fix to exit criterion of the velocity solver with an absolute tolerance of `1.0E-16` and vary the one for the Poisson solver (between `1.0E-05` and `1.0E-16`).

The solution is computed on a 2D structured stretched Cartesian grid that covers a `30cx30c` domain with the immersed boundary 
(with chord-length `c`) centered in it.
The spatial discretization is uniform in the region `[-0.51966, 3.48]x[-1.99983, 1.99983]` with grid-spacing `0.00267`.
Outside, the gridlines are stretched with constant ratio `1.01` in all directions.

To avoid the transient regime due to the impulsively start, we first compute `1000` time-steps (i.e., `0.1` non-dimensional time-unit) using smallest absolute tolerance for the Poisson solver.

```
time $CUIBM -caseFolder atol16
```

where `$CUIBM` is the path to the cuIBM executable.

The solution at `0.1` time-unit was then used to compute an extra `500` time-steps for each absolute tolerance of the Poisson solver.

```
cp -r atol16/0001000 atolx/
time $CUIBM -caseFolder atolx
```

for `x` in `{5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}`.

We consider the solution obtained with the smallest absolute tolerance as the machine-accurate one.
At time-step `1500`, we compare the differences in the forces, the flux fields, and the pressure fields from each run with the machine-accurate solution.
The is done with the Python script `plotIterativeErrors.py`.

We used the version of cuIBM tagged [`snake-repro-cusp-0.5.1`](https://github.com/barbagroup/cuIBM/releases/tag/snake-repro-cusp-0.5.1), the linear algebra library [`CUSP-0.5.1`](https://github.com/cusplibrary/cusplibrary/releases/tag/v0.5.1), and `CUDA-7.5`.

Each run requires about 6GB of memory on the GPU device.
We used a GPU K40 to compute the solutions.