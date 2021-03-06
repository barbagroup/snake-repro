##Story 1: Meshing and boundary conditions can ruin everything

Generating good meshes for discretization  is probably the most vexing chore of computational fluid dynamics. 
And stipulating boundary conditions on the edge of a mesh takes some nerve, too. 
An early example of how frustrating it can be to investigate different outflow boundary conditions is reported in \citet{SaniGresho1994}. 
Our first attempts at a full replication study of the 2D snake aerodynamics with IcoFOAM, the incompressible laminar Navier-Stokes solver of OpenFOAM, showed us just how vexing and unnerving these issues can be.

OpenFOAM can take various types of mesh as input. 
One popular mesh generator is called GMSH: it produces triangles that are as fine as you want them near the body, while getting coarser as the mesh points are farther away. 
Already, we encounter a problem: how to create a mesh of triangles that gives a comparable resolution to that obtained with our original structured Cartesian mesh? 
After dedicated effort, we produced the best mesh we could that matches our previous study in the finest cell width near the body. 
But when using this mesh to solve the fluid flow around the snake geometry, we got spurious specks of high vorticity in places where there shouldn’t be any (Figure 1). 
Even though the meshes passed the OpenFOAM quality checks, these unphysical vortices appeared for any flow Reynolds number or body angle of attack we tried—although they were not responsible for the simulations to blow up (fail due to rapid error growth).
Finally, we gave up with the (popular) GMSH and tried another mesh generator: SnappyHexMesh (details and plots of the meshes are included in the supplementary materials). 
Success! 
No unphysical patches in the vorticity field this time. 
But another problem persisted: after the wake vortices hit the edge of the computational domain in the downstream side, a nasty back pressure appeared there and started propagating to the inside of the domain (Figure 2). 
This situation is also unphysical, and we were certain there was a problem with the chosen outflow boundary condition in OpenFOAM, but did not find any way to stipulate another, more appropriate boundary condition. 
We used a zero-gradient condition for the pressure at the outlet (and tried several other possibilities), which we found was a widespread choice in the examples and documentation of OpenFOAM. 
After months, one typing mistake when launching a run from the command line made OpenFOAM print out the set of available boundary conditions, and we found that an _advective_ condition was available that could solve our problem. 
All this time, we were looking for a _convective_ condition, which is just another name for the same thing: satisfying a linear convection equation at the boundary points. 
Finally, simulations with OpenFOAM were looking correct—and happily, the main feature of the aerodynamics was replicated: an enhanced lift coefficient at 35º angle-of-attack (Figure 3). 
But not all is perfect. 
The time signatures of lift and drag coefficient do show differences between our IcoFOAM calculation and the original published ones (Figure 4). 
The key finding uses an _average_ lift coefficient, calculated with data in a time range that is reasonable but arbitrary. 
Refining the mesh or reducing the exit criterion of the iterative solvers made a difference of less than 0.5% in this quantity.
The average force coefficients match (within < 3%) our previous results, despite the differences seen on the time series. 
Are these the same solutions? 
Is it acceptable as a replication study? 
We think yes, but this is a judgement call.