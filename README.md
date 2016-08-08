## *"Reproducible and replicable CFD: it's harder than you think"*

(c) Olivier Mesnard, Lorena A. Barba, 2016.

Article submitted on 13 May 2016. Preprint on [arXiv:1605.04339](http://arxiv.org/abs/1605.04339)

Decision 25 July 2016: Accept with minor revisions, _Computing in Science and Engineering_.

### Contents

This repository contains the manuscript source files, and supplementary materials including input files, geometry files, running scripts and Jupyter notebooks for all runs reported on in the paper. 

The notebook [`tableOfContents`](https://github.com/barbagroup/snake-repro/blob/master/reproducibilityPackages/tableOfContents.ipynb) lists the simulations reported in the paper, with a link to their respective `report` notebook.

In each notebook, we include information about the dependencies needed by each code, the mesh information, the boundary conditions, the parameters for each linear solver, the command-line input to run the simulation and finally the Python post-processing scripts to generate the figures.

---

The article reports on a full replication study of our previously published findings on bluff-body aerodynamics of flying snakes ([Krishnan et al., 2014](http://scitation.aip.org/content/aip/journal/pof2/26/3/10.1063/1.4866444)).

Over the span of about three years, we ran hundreds of simulations of the flow around a 2D snake geometry, using four different flow solvers. 
The paper reports on 40 of these runs, telling the story of our mistakes and challenges to complete the replication of our previous findings. 

We prepared detailed *"Reproducibility packages"* for each one of the simulations reported in the paper; they are in the `/reproducibilityPackages` directory. 
Each simulation folder contains a Jupyter Notebook, named `report`, with all the information about the case, and all the data needed to reproduce the calculation. 

The folder `figures` contains all the plots and flow visualizations included in the paper. 
The Python and bash scripts we used to generate the figures are in the folder `reproducibilityPackages/figures`.

To postprocess and compare the numerical solution from the 4 different codes, we developed a Python package called [`snake`](https://github.com/mesnardo/snake), hosted on GitHub under the MIT License.


We used a total of four CFD solvers in the study:

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



---

LICENSE -- Not all content in this repository is open source. The Python code only is shared under an MIT License. The written content in the Jupyter Notebooks is shared under a Creative Commons Attribution (CC-BY) license. But *please note that the manuscript text is not open source*; we reserve rights to the article content, which is currently submitted for publication in a journal. Only fair use applies in this case.

## References

* Krishnan, Anush, John J. Socha, Pavlos P. Vlachos, L. A. Barba (2014), Lift and wakes of flying snakes. _Physics of Fluids_ *26*, 031901, [doi:10.1063/1.4866444](http://dx.doi.org/10.1063/1.4866444)
* Krishnan, Anush,  John J. Socha, Pavlos P. Vlachos, L. A. Barba (2013), Body cross-section of the flying snake Chrysopelea paradisi. figshare.
[doi:10.6084/m9.figshare.705877.v1](https://dx.doi.org/10.6084/m9.figshare.705877.v1)