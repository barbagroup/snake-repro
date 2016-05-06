Our research group prides itself for having adopted Reproducible Research practices. 
Barba made a public pledge titled *"Reproducibility PI Manifesto"* ^(1) (PI: Principal Investigator), which at the core is a promise to make all research materials and methods open access and discoverable: releasing code, data and analysis/visualization scripts.

In 2014, we published a study on Physics of Fluids titled *"Lift and wakes of flying snakes."* ^(2) 
It is a study that uses our in-house code for solving the equations of fluid motion in two dimensions, with a solution approach called “immersed boundary method.” 
The key of such a method for solving the equations is that it exchanges complexity in the mesh generation step for complexity in the application of boundary conditions. 
It makes possible using a simple discretization mesh (structured Cartesian), but at the cost of an elaborate process that interpolates values of fluid velocity at the boundary points to ensure the no-slip boundary condition (that fluid sticks to a wall). 
The main finding of our study on wakes of flying snakes was that the 2D section with anatomically correct geometry for the snake’s body experiences lift enhancement at a given angle of attack.
A previous experimental study had already shown that the lift coefficient of a snake cross section in a wind tunnel gets an extra oomph of lift at 35º angle-of-attack. 
Our simulations showed the same feature in the plot of lift coefficient. 
Many detailed observations of the wake (visualized from the fluid-flow solution in terms of the vorticity field in space and time) allowed us to give an explanation of the mechanism providing extra lift.

When a computational research group produces this kind of study with an in-house code, it can take one, two or even three years to write a full research software from scratch, and complete verification and validation. 
Often, one gets the question: why not use a commercial CFD package? (CFD: computational fluid dynamics.) 
Why not use another research group’s open-source code? 
Doesn't it take much longer to write yet another CFD solver than to use existing code? 
Beyond reasons that have to do with inventing new methods, it’s a good question. 
To explore using an existing CFD solver for future research, we decided to first complete a full replication of our previous results with these alternatives. 
Our commitment to open-source software for research is unwavering, which rules out commercial packages. 
Perhaps the most well known open-source fluid-flow software is OpenFOAM, so we set out to replicate our published results with this code. 
A more specialist open-source code is IBAMR, a project born at New York University that has continued development for half a decade. And finally, our own group developed a new code, implementing the same solution method, but providing parallel computing via the renowned PETSc library. We embarked on a full replication study of our previous work, using three new fluid-flow codes.

This is the story of what happened next: three years of dedicated work that encountered a dozen ways that things can go wrong, conquered one after another, to arrive finally at (approximately) the same findings and a whole new understanding of what it means to do “reproducible research” in computational fluid dynamics.

--

> ###Fluid-flow solvers we used
> **cuIBM**--- Used for our original study (Krishan et al., 2014), this code is written in C CUDA to exploit GPU hardware, but is serial on CPU. 
> It uses the NVIDIA *Cusp* library for solving sparse linear systems on GPU. 
> <https://github.com/barbagroup/cuIBM>  
> **OpenFOAM**--- A free and open-source CFD package that includes a suite of numerical solvers.
> The core discretization scheme is a finite-volume method applied on mesh cells of arbitrary shape. 
> <http://www.openfoam.org>  
> **IBAMR**--- A parallel code using the immersed boundary method on Cartesian meshes, with adaptive mesh refinement.
> <https://github.com/ibamr/ibamr>  
> **PetIBM**--- This is our own re-implementation of *cuIBM*, but for distributed-memory parallel systems.
> It uses the PETSc library for solving sparse linear systems in parallel.
> <https://github.com/barbagroup/PetIBM> 

--

### Story 1: Meshing and boundary conditions can ruin everything

Generating good discretization meshes is probably the most vexing chore of computational fluid dynamics. 
And stipulating boundary conditions on the edge of a discretization mesh takes some nerve, too. 
Our first attempts at a full replication study of the 2D snake aerodynamics with OpenFOAM showed us just how vexing and unnerving this can be.

OpenFOAM can take various types of discretization mesh as input. 
One popular mesh generator is called GMSH: it produces triangles that are as fine as you want them near the body, while getting coarser as the mesh points are farther away. 
Already, we encounter a problem: how to create a mesh of triangles that gives a comparable resolution to that obtained with our original structured Cartesian mesh? 
After dedicated effort (see separate section on mesh generation with OpenFOAM [or supplementary material?]), we produced the best mesh we could that matches our previous study in the finest cell width near the body. 
But when using this mesh to solve the fluid flow around the snake geometry, we got spurious specks of high vorticity in places where there shouldn’t be any. 
The simulations did not blow up, but these unphysical vortices appeared for any flow Reynolds number or body angle of attack we tried.
This is despite the fact that the mesh passed the quality checks of OpenFOAM. 
Finally, we gave up with the (popular) GMSH and tried another mesh generator: SnappyHexMesh. 
Success! 
No unphysical patches in the vorticity field this time. 
But another problem persisted: after the wake vortices hit the edge of the computational domain in the downstream side, a nasty back pressure appeared there and started propagating to the inside of the domain. 
This situation is also unphysical, and we were certain there was a problem with the chosen outflow boundary condition in OpenFOAM, but did not find any way to stipulate another, more appropriate boundary condition. 
We used a zero-gradient condition for the pressure at the outlet, which we found was a widespread choice in the examples and documentation of OpenFOAM. 
After months, one typing mistake when launching a run from the command line made OpenFOAM print out the set of available boundary conditions, and we found that an _advective_ condition was available that could solve our problem (all this time, we were looking for _convective_ condition, which is just another name for the same thing). 
Finally, simulations with OpenFOAM were looking correct—and happily, the main feature of the aerodynamics was replicated: an enhanced lift coefficient at 35º angle-of-attack. 
But not all is perfect. 
The time signatures of lift and drag coefficient do show differences between our OpenFOAM calculation and the original published ones. 
The key finding uses an _average_ lift coefficient, calculated with data in a time range that is reasonable but arbitrary. 
Although the average force coefficients match (within <3%) our previous results, the time series shows a phase difference. 
Are these the same solutions? 
Is it acceptable as a replication study? 
We think yes, but this is a judgement call.

**Postmortem**. 
OpenFOAM solves the fluid equations using a finite-volume method in an unstructured grid, while our published study used an immersed boundary method in a stretched Cartesian grid. 
Comparing results obtained under such different conditions is a delicate operation. 
We made our best attempt at creating a fluid mesh for OpenFOAM that was of similar resolution near the body as we had used before. 
But unstructured grids are complex geometrical objects. 
Two meshes built with the same parameters will not be exactly the same, even. 
The complication of building a _good quality_ mesh is one of the reasons some prefer immersed boundary methods!

### Story 2: Other researchers' open-source codes come with traps

Open-source research software can often be poorly documented and unsupported, and on occasion it can even be an unreadable mess. 
But in this case, we are in luck.
IBAMR is a solid piece of software, well documented, and you can even get swift response from the authors via the topical online forum.
Still, we ran against an obscure trick of the trade that changed our results completely. 

The numerical approach in IBAMR belongs to the same family as that used in our published work on wakes of flying snakes: an immersed boundary method. 
The essence of the approach is that the fluid is represented by a fixed structured mesh, while the immersed body is represented by its own, separate mesh that moves with the body. 
We speak of an Eulerian mesh for the fluid, and a Lagrangian mesh for the solid. 
The forces exerted by the fluid on the body, and vice versa, appear as an additional integral equation and interpolation schemes between the two meshes. 
The role of these is to make the fluid "stick" to the wall (no-slip boundary condition) and allow the body to feel aerodynamic forces (lift and drag).
Our cuIBM code uses a variant called the immersed boundary projection method, while IBAMR uses a form called the "direct-forcing" method. 
Despite the variations, the essence is the same, and it is reasonable to assume they would work similarly.

We already know that boundary conditions at the outlet of the computational domain can be problematic. This is no different with immersed boundary methods. 
Our first attempt with IBAMR used a zero-gradient velocity boundary condition at the outlet. 
This resulted in some blockage effect when the wake vortices reach the domain boundary: strong vorticity rebounds from the artificial boundary and propagates back to the domain. 
Of course, this is unphysical and the result unacceptable. 
After a long search in the literature and in the code documentation, we discovered that IBAMR needs us to select a "stabilized outlet," which is a boundary condition that acts like a force pushing the vortices out. 
(IBAMR does not provide a convective/advective boundary condition.) 
With this new configuration, the simulations of the snake profile resulted in a wake that looked physical, but a computed lift coefficient that was considerably different from our published study. 
Another deep dive in the literature led us to notice that a benchmark example described in the paper that announced IBAMR was set up in an unexpected way: 
the no-slip condition is forced _inside_ the body, and not just on the boundary. 
As far as we could find, the publications using IBAMR are the only cases where interior points are constrained. 
Other papers using immersed boundary methods apply the constraint only on boundary points.
When we followed their example, our simulations with IBAMR were able to reproduce the lift enhancement at 35 degress angle-of-attack, although with a slightly different value of lift (<5% off). 
The successful result comes with a caveat, though. 
If we look at the time signature of the lift and drag coefficients, there is excellent agreement with our previous results for 30 degress angle-of-attack (Re-2000). 
But at 35 degress, the time signatures drift apart after about 40 time units (10,000 time steps). 
There is a marked drop in the lift coefficient, but because the average is calculated over a time range between 32 and 64 time units (a reasonable but arbitrary choice), the final numeric result is not far off our published study. 
 
**Postmortem**. 
Even a well-documented open-source research code can have unexpected tricks of the trade that only the original authors may know about. 
In the end, we don't have an explanation for _why_ IBAMR required interior body points to be constrained. 
The published record is incomplete in this regard: we could find no explanation in any paper using IBAMR. 
Using an open research code and getting correct results with it could involve a long investigative period, potentially requiring communication with the original authors and many failed attempts. 
If the code is not well documented and the original authors are not responsive to questions, then building your own code from scratch could be more sensible!

### Story 3: A different external linear algebra library can fail your replication

The immersed-boundary projection-method requires the solution of two linear systems (an intermediate velocity system and a modified-Poisson system) every time-step of the simulation.
As it is commonly done in CFD research-codes, we rely on an external linear algebra library.
Our previous publication reports simulations with cuIBM, an in-house code that uses the library CUSP to solve the linear systems on a single-GPU.
With cuIBM, we were limited to small mesh-sizes to not exceed the memory capacity of the device.
As a workaround, we decided to develop PetIBM, CPU-based code that runs on distributed-memory architectures.
PetIBM implements the same mathematical formulation of the immersed-boundary method than cuIBM.
We replaced the GPU-library CUSP with the well-known PETSc-library (version 3.5.2); therefore, solving the linear systems on a different hardware.
Both libraries use the same convergence criterion for the linear solvers.
As a verification test-case, we ran the snake simulations to compare with previous cuIBM results.
The results did not fully meet our expectations.
Comparing the instantaneous force coefficients with those reported with cuIBM, we find some discrepancies as the we increase the Reynolds number and the angle-of-attack of the snake cross-section.
We failed to replicate of our own findings: we did not observe a lift enhancement of the snake cross-section for the particular angle-of-attack 35 degrees.
The instantaneous force coefficients closely follows the cuIBM ones up to 35 time-units of flow simulation.
Afterwards, we observe drop in the mean force coefficients.
Consequently, if we use the same time-integration period (32 to 64 time-units) to average the force coefficients, we are not able to observe a pick in the lift-curve.
While we were checking the PetIBM simulations parameters were identical to the cuIBM ones, we found that the set of markers used to discretized the immersed-boundary were a little bit shifted (less than an edge of the finest grid-cell) compared the our previous study.
This displacement happened as we have not rotated the geometry around the same center to provide the desired pitch angle.
Our new hope rapidly vanished when we saw that the same set of markers did not provide the same extra-lift than in our previous study.
Visualizations of the wake vortices show that a vortex merging phenomenon occurred in the middle of the wake affecting the near-body flow and lowering the forces on the bluff-body.
The vortex merging affects the near-wake signature: the previously aligned vortices now form a wider wake with a 1S+1P pattern (a single clockwise vortex on the top side and a vortex dipole on the bottom part).
We also note that a small shift in the Lagrangian markers is responsible for a significant change in the forces acting on the snake at moderate Reynolds number 2000.
Although PetIBM implements the same immersed-boundary method and was developed by the same research-group, we have not been able to fully replicate the findings of our previous study.

### Story 4: How much reproducible is our research?

As mentioned early, our previous study was published under the "Reproducibility PI Manifesto" with the code and the data being openly shared; thus, we decided to reproduce our own findings.
From the time of our previous publication to now, the lab-machines have changed a lot: new operating systems, new GPU devices, new external libraries.
The code itself has been modified as new has been implemented.
Therefore, we tried to reproduce our own results using (1) the "same" version of the code and (2) the current version of cuIBM.
In both cases, we used identical input parameters (Lagrangian markers to discretize the geometry, grid parameters, flow conditions, and solvers parameters).

As mentioned before, we use the library CUSP to solve the linear system on a GPU.
The two-year-old simulations used a version of CUSP that is not longer compatible with the cuda versions installed on our machines.
Thus, we adapted cuIBM to be compatible with a newer version of CUSP (0.4.0).
We ran a simulation of the snake at angle-of-attack 35 degrees and Reynolds number 2000.
We observe some discrepancies in the force coefficients generated by the bluff-body over the end of time-integration period: the mean force coefficients drop between 60 and 80 time-units.
This has not been observed in our previous study.

In addition, we ran the same application with the actual version of cuIBM comparing two version of the library CUSP (0.4.0 and 0.5.1).
We first notice that the actual cuIBM version with the same CUSP library leads to the same force signals than the previous cuIBM version.
Second, we observe differences when using different CUSP versions, only when the mean force coefficients are dropping -- up to 70 time-units, the difference is negligible.

Although the instantaneous force coefficients exhibit some numerical differences over the end of the flow simulation, if we averaged them during the same time-interval than in our previous publication, we obtain the similar enhanced lift coefficients acting on the snake cross-section at angle-of-attack 35 degrees and Reynolds number 2000.
Therefore, we are been able to reproduce our previous results to a certain level.


Therefore, searching for the same numerics sound like a crazy idea.
But what does it really mean to do reproducible research?




## References

1. ICERM Workshop on Reproducibility in Computational and Experimental Mathematics (December 10-14, 2012), https://icerm.brown.edu/tw12-5-rcem/
2. Krishnan, A., Socha, J. J., Vlachos, P. P., & Barba, L. A. (2014). Lift and wakes of flying snakes. Physics of Fluids, 26(3), 031901.