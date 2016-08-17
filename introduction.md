Our research group prides itself for having adopted Reproducible Research practices. 
\citet{barba2012} made a public pledge titled *"Reproducibility PI Manifesto"* (PI: Principal Investigator), which at the core is a promise to make all research materials and methods open access and discoverable: releasing code, data and analysis/visualization scripts.

In 2014, we published a study on Physics of Fluids titled *"Lift and wakes of flying snakes"* \citep{krishnan2014}. 
It is a study that uses our in-house code for solving the equations of fluid motion in two dimensions (2D), with a solution approach called the “immersed boundary method.” 
The key of such a method for solving the equations is that it exchanges complexity in the mesh generation step for complexity in the application of boundary conditions. 
It makes it possible to use a simple discretization mesh (structured Cartesian), but at the cost of an elaborate process that interpolates values of fluid velocity at the boundary points to ensure the no-slip boundary condition (that fluid sticks to a wall). 
The main finding of our study on wakes of flying snakes was that the 2D section with anatomically correct geometry for the snake’s body experiences lift enhancement at a given angle of attack.
A previous experimental study had already shown that the lift coefficient of a snake cross section in a wind tunnel gets an extra oomph of lift at 35 degrees angle-of-attack. 
Our simulations showed the same feature in the plot of lift coefficient \citep{krishnan2013}. 
Many detailed observations of the wake (visualized from the fluid-flow solution in terms of the vorticity field in space and time) allowed us to give an explanation of the mechanism providing extra lift.
The flow around the snake's body cross section adopts a pattern known as a von Karman vortex street. 
It is a particularly complex flow, because it involves three shear layers: the boundary layer, a separating free shear layer, and the wake \citep{Williamson_1996}. 
Physically, each of these shear layers is subject to instabilities. 
The free shear layer can experience 2D Kelvin-Helmholtz instability, while the wake experiences both 2D and 3D instabilities and can show chaotic behavior. 
Such flows are particularly challenging for computational fluid dynamics (CFD).

When a computational research group produces this kind of study with an in-house code, it can take one, two or even three years to write a full research software from scratch, and complete verification and validation. 
Often, one gets the question: why not use a commercial CFD package?  
Why not use another research group’s open-source code? 
Doesn't it take much longer to write yet another CFD solver than to use existing code? 
Beyond reasons that have to do with inventing new methods, it’s a good question. 
To explore using an existing CFD solver for future research, we decided to first complete a full replication of our previous results with these alternatives. 
Our commitment to open-source software for research is unwavering, which rules out commercial packages. 
Perhaps the most well known open-source fluid-flow software is OpenFOAM, so we set out to replicate our published results with this code. 
A more specialist open-source code is IBAMR, a project born at New York University that has continued development for a decade. 
And finally, our own group developed a new code, implementing the same solution method we had before, but providing parallel computing via the renowned PETSc library. 
We embarked on a full replication study of our previous work, using three new fluid-flow codes.

This is the story of what happened next: three years of dedicated work that encountered a dozen ways that things can go wrong, conquered one after another, to arrive finally at (approximately) the same findings and a whole new understanding of what it means to do “reproducible research” in computational fluid dynamics.
