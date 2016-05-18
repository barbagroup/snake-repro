# Reproducibility packages

For the article:

### "Reproducible and replicable CFD: it's harder than you think"

Olivier Mesnard, Lorena A. Barba

Article submitted on 13 May 2016. Preprint on [arXiv:1605.04339]((http://arxiv.org/abs/1605.04339))
---

We used a total of four CFD solvers in this study:

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


The article reports on the numerical solution from 40 simulations. We prepared detailed *"Reproducibility packages"* for each one of these simulations, which are found in the `/reproducibilityPackages` directory. 
Each simulation folder contains a Jupyter Notebook, named `report`, with all the information about the case, the command-lines input to run the simulation, and the Python codes to pre- and post-process the simulation.
The notebook `tableOfContents` lists the simulations with a link to their respective `report` notebook.

The folder `snakePaperFigures` contains the Python and bash scripts we used to generate the figures in the manuscript.

To postprocess and compare the numerical solution from the 4 different codes, we developed a Python package called [`snake`](https://github.com/mesnardo/snake) and hosted on GitHub under the MIT License.

---

LICENSE -- Not all content in this repository is open source. The Python code only is shared under an MIT License. The written content in the Jupyter Notebooks is shared under a Creative Commons Attribution (CC-BY) license. But *please note that the manuscript text is not open source*; we reserve rights to the article content, which is currently submitted for publication in a journal. Only fair use applies in this case.