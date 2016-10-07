The present directory reports on simulations run with cuIBM, PetIBM, IBAMR, and OpenFOAM to assess the independence of the numerical solution when changing the parameters such as the spatial discretization, the temporal discretization, and the exit criterion of the iterative solvers.

## Table of Contents:

* [cuIBM's results](./cuibm/report.ipynb): grid-independence, iterative-convergence in the residuals, and temporal convergence in the forces acting on the flying-snake cross-section at Reynolds number 2000.

* [PetIBM's results](./petibm/report.ipynb): grid-independence, iterative-independence in the residuals, and temporal-independence in the forces at Reynolds number 2000.

* [IBAMR's results](./ibamr/report.ipynb): evaluation of the relative differences in the force coefficients due to iterative errors and temporal errors at Reynolds number 2000.

* [OpenFOAM's results](./openfoam/report.ipynb): grid-independence and iterative-independence analysis at Reynolds number 2000 and angle-of-attack 35 degrees.