## Lessons learned

Reproducibility and replication of studies are essential for the progress of science, and much of science today advances via computation. 
We use computer simulations to create new knowledge. 
How can we certify that this new knowledge is justified, that there is enough evidence to support it? 
The truth is computational science and engineering lacks an accepted standard of evidence. 
We label computational research *reproducible* when authors provide all the necessary data and the computer code to run the analysis again, re-creating the results. 
But what data are necessary? 
We found that open-source code and open data sets are a minimal requirement. 
Exhaustive documentation during the process of computational research is key. 
This includes documenting all failures. 
Current publication custom is biased towards positive results \citep{Ioannidis_2005}. 
The CFD community does not have a habit of communicating negative results; 
one rare example is the analysis of Godunov methods and its failures by \citet{quirk1997}.
In the case of IBAMR, negative results with points only on the boundary are not among the examples provided: the situation may be obvious to the authors, but not to the users. 
We learned how important the computational mesh and the boundary conditions can be. 
A reproducible computational paper should include the actual meshes used in the study (or a deterministic mesh-generation code) and careful reporting of boundary conditions. 
This is rarely (if ever!) the case. 
We learned that in addition to developing our code under version control, we need to carefully record the versions used for all dependencies. 
In practice, such careful documentation is feasible only with a fully automated workflow: 
launching simulations via running scripts, storing command-line arguments for every run, capturing complete environment settings. 
Post-processing and visualization ideally should also be scripted, avoiding software GUIs for manipulation of images. 

We learned that highly unsteady fluid dynamics is a particularly tough application for reproducibility. 
The Navier-Stokes equations are nonlinear and can exhibit chaotic behavior under certain conditions (e.g., geometry, Reynolds number, external forcing). 
Some flow situations are subject to instabilities, like vortex merging in two dimensions and other vortex instabilities in 3D. 
In any application that has sufficient complexity, we should repeat simulations checking how robust they are to small variations. 
And report negative results! 
Understandably, long 3D simulations that take huge computational resources may not be feasible to repeat. 
We should continue the conversation about what it means to do reproducible research in high-performance computing (HPC) scenarios. 
When large simulations run on specific hardware with one-off compute allocations, they are unlikely to be reproduced. 
In this case, it is even more important that researchers advance towards these HPC applications on a solid progression of fully reproducible research at the smaller scales. 

Computational science and engineering makes ubiquitous use of linear algebra libraries like PETSc, Hypre, Trilinos and many others. 
Rarely do we consider that using different libraries might produce different results. 
But that is the case. 
Sparse iterative solvers use various definitions of the _tolerance_ criterion to exit the iterations, for example. 
The very definition of _residual_ could be different. 
This means that even when we set the same value of the tolerance, different libraries may declare convergence differently! 
This poses a challenge to reproducibility, even if the application is not sensitive to algebraic error. 
The situation is aggravated by parallel execution. 
Global operations on distributed vectors and matrices are subject to rounding errors that can accumulate to introduce uncertainty in the results. 

We are recommending more rigorous standards of evidence for computational science and engineering, but the reality is that most CFD papers are not even accompanied by a release of code and data. 
The reasons for this are varied: historical, commercial interests, academic incentives, time efficiency, etc. 
The origins of CFD in the Los Alamos Laboratory in the 1940s was secret research, and when computer code was stored in large boxes of punched cards, there was hardly a way to "share" it \citep{metropolis1982}. 
The 1970s saw the birth of commercial CFD, when university professors and their students founded companies funded under the US government's SBIR program. 
It’s not unreasonable to speculate that the potential for commercial exploitation was a deterrent for open-source release of CFD codes for a long time. 
It is only in the last 15 years or so that open-source CFD codes have become available. 
But the CFD literature became entrenched in the habit of publishing results without making available the code that generated those results. 
And now, we face the clash between the academic incentive system and the fact that reproducible research takes a substantial amount of time and effort. 
This campaign to replicate our previous results taught us many lessons on how to improve our reproducibility practices, and we are committed to maintaining this high standard. 
We will continue to share our experiences.
