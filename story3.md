### Story 3: All linear algebra libraries are not created equal

Our previous study used cuIBM, running on a single GPU device. 
The largest problem that we can fit in the memory of a high-end GPU has just a few million mesh points, which is not enough to solve three-dimensional flows. 
We developed PetIBM, a code that uses the same mathematical formulation as cuIBM, to allow solving larger problems on distributed CPU systems. 
Since PetIBM and cuIBM implement exactly the same numerical method, you'd expect that giving the two codes the same mesh with the same initial conditions will result in the same solution (within floating-point error). 
Not so fast! 
We rely on external libraries to solve sparse linear systems of equations: _Cusp_ for GPU devices and PETSc for distributed CPU systems. 
It turns out, the iterative solvers may have differences that affect the final solution.

When repeating our previous simulations of the aerodynamics of a snake cross-section with PetIBM, the solutions do not always match those computed with cuIBM. 
At a Reynolds number of 1000, both the time-averaged lift and drag coefficients match. 
But at Reynolds equal to 2000, average lift and drag match up to 30 degrees angle-of-attack, but not at 35 degrees. 
That means that we don't see lift enhancement (Figure 8) and the main finding of our previous study is not fully replicated. 
Looking at the time evolution of the force coefficients for the simulation with PetIBM at Re=2000 and 35 degrees angle-of-attack, we see a marked drop in lift after 35 time units (top graph in Figure 9). 
What is different in the two codes? 
Apart from using different linear algebra libraries, they run on different hardware. 
Leaving hardware aside for now, let's focus on the iterative solvers. 
Both _Cusp_ and PETSc use the same convergence criterion. 
This is not always the case, and needs to be checked! 
We're also not using the same iterative solver with each library. 
The cuIBM runs (with _Cusp_) used an algebraic multigrid preconditioner and conjugate gradient (CG) solver for the modified-Poisson equation. 
With PETSc, the CG solver crashed because of an indefinite preconditioner (having both positive and negative eigenvalues), and we had to select a different method: we used a bi-CG stabilized algorithm (while still using an algebraic multigrid preconditioner). 

Could this difference in linear solvers affect our unsteady fluid-flow solution? 
The solutions with both codes match at lower angles of attack (and lower Reynolds numbers), so what is going on? 
We checked everything multiple times. 
In the process, we did find some small discrepancies. 
Even a small bug (or two).
We found, for example, that the first set of runs with PetIBM created a slightly different problem set-up, compared with our previous study, where the body was shifted by less than one grid-cell width. 
Rotating the body to achieve different angles of attack was made around a different center, in each case (one used the grid origin at 0,0 while the other used the body center of mass). 
This tiny difference does result in a different average lift coefficient (bottom graph in Figure 9)! 
The time signal of lift coefficient shows that the drop we were seeing at around 35 time units now occurs closer to 50 time units, resulting in a different value for the average taken in a range between 32 and 64. 
Again, this range for computing the average is a choice we made. 
It covers about ten vortex shedding cycles, which seems enough to calculate the average if the flow is periodic.
What is causing the drop in lift? 
Visualizations of the wake vortices (Figure 10) show that a vortex-merging event occurs in the middle of the wake, changing the near-wake pattern. 
The previously aligned positive and negative vortices are replaced by a wider wake with a single clockwise vortex on the top side and a vortex dipole on the bottom part. 
With the change in wake pattern comes a drop in the lift force. 
