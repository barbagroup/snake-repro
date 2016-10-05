# Flying-snake, Re=2000, AoA=35deg, h=0.006

The present directory contains all input files to compute with cuIBM the flow around a flying-snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000.

We compute 80 non-dimensional time-units on a 2D structured stretched Cartesian grid that covers a `30cx30c` domain with the immersed boundary 
(with chord-length `c`) centered in it.
The spatial discretization is uniform in the region `[-0.516, 3.48]x[-1.998, 1.998]` with grid-spacing `0.006`.
Outside, the gridlines are stretched with constant ratio `1.01` in all directions.

The bash script `preprocessing.sh`:
- creates the file `domain.yaml` that contains the information about the spatial discretization in a YAML format;
- generates the coordinates of the immersed boundary with resolution h=0.006 (distance between two consecutive points).

To run the simulation:

    time $CUIBM -caseFolder $SIMU_DIR

where `$CUIBM` is the path to the cuIBM executable and `$SIMU_DIR` is the directory with the input files.

We used the version of cuIBM tagged [`snake-repro-cusp-0.5.1`](https://github.com/barbagroup/cuIBM/releases/tag/snake-repro-cusp-0.5.1), the linear algebra library [`CUSP-0.5.1`](https://github.com/cusplibrary/cusplibrary/releases/tag/v0.5.1), and `CUDA-7.5`.

The simulation requires about 2GB of memory on the GPU device.
We used a GPU K20 and computed the solution up to 80 non-dimensional time-units (`400k` time-steps with time-increment `0.0002`) in approximatively 6 days.