# Reproducibility packages

### [*"Reproducible and replicable CFD: it's harder than you think"*](http://arxiv.org/abs/1605.04339)

Olivier Mesnard, Lorena A. Barba

---

In our attempt to reproduce and replicate our own previous findings on the aerodynamics of the flying-snake ([Krishnan et al., 2014](http://scitation.aip.org/content/aip/journal/pof2/26/3/10.1063/1.4866444)), we used a total of four CFD software:

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


In our manuscript, [*"Reproducible and replicable CFD: it's harder than you think"*](http://arxiv.org/abs/1605.04339), we report the numerical solution from 40 simulations.

The following directory contains the input files necessary to re-run each one of the 40 simulations.
In addition, each simulation folder contains a Jupyter-Notebook, named `report`, with all information about the case, the command-lines to run the simulation, and Python codes to pre- and post-process the simulation.
On top of that, the notebook `tableOfContents` lists the simulations with a link to their respective notebook.

Moreover, the folder `snakePaperFigures`, contains the Python and bash scripts we used to generate the figures of the manuscript.

To post-process and compare the numerical solution from the 4 different softwares, we developed a Python package, called `snake`, hosted on [GitHub](https://github.com/mesnardo/snake) under the MIT License.