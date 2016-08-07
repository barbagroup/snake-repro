> **Fluid-flow solvers we used**
> **cuIBM**--- Used for our original study (Krishan et al., 2014), this code is written in C CUDA to exploit GPU hardware, but is serial on CPU. 
> It uses the NVIDIA *Cusp* library for solving sparse linear systems on GPU. 
> <https://github.com/barbagroup/cuIBM>  
> **OpenFOAM**--- A free and open-source CFD package that includes a suite of numerical solvers.
> The core discretization scheme is a finite-volume method applied on mesh cells of arbitrary shape. 
> <http://www.openfoam.org>  
> **IBAMR**--- A parallel code using the immersed boundary method on Cartesian meshes, with adaptive mesh refinement.
> <https://github.com/ibamr/ibamr>  
> **PetIBM**--- Our own re-implementation of *cuIBM*, but for distributed-memory parallel systems.
> It uses the PETSc library for solving sparse linear systems in parallel.
> <https://github.com/barbagroup/PetIBM> 


