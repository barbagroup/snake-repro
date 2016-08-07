## Story 2: Other researchers' open-source codes come with traps

Open-source research software can often be poorly documented and unsupported, and on occasion it can even be an unreadable mess. 
But in this case, we are in luck.
IBAMR is a solid piece of software, well documented, and you can even get swift response from the authors via the topical online forum.
Still, we ran against an obscure trick of the trade that changed our results completely. 

The numerical approach in IBAMR belongs to the same family as that used in our published work on wakes of flying snakes: an immersed boundary method. 
The essence of the approach is that the fluid is represented by a structured mesh, while the immersed body is represented by its own, separate mesh that moves with the body. 
We speak of an Eulerian mesh for the fluid, and a Lagrangian mesh for the solid. 
The forces exerted by the fluid on the body, and vice versa, appear as an additional integral equation and interpolation schemes between the two meshes. 
The role of these is to make the fluid "stick" to the wall (no-slip boundary condition) and allow the body to feel aerodynamic forces (lift and drag).
IBAMR implements a subclass of the immersed-boundary method called the direct-forcing method suitable for rigid bodies.
Our cuIBM code uses a variant called the immersed-boundary projection method.^(4) 
Despite the variations, the essence is the same, and it is reasonable to assume they would work similarly.

We already know that boundary conditions at the outlet of the computational domain can be problematic. 
This is no different with immersed boundary methods. 
Our first attempt with IBAMR used a zero-gradient velocity boundary condition at the outlet. 
This resulted in a spurious blockage of the wake vortices when they reach the domain boundary: strong vorticity rebounds from the artificial boundary and propagates back to the domain (Figure 5). 
Of course, this is unphysical and the result is unacceptable. 

After a long search in the literature and in the documentation, it was through a conversation with the main developers on the online forum that we discovered the solution: using a "stabilized outlet" boundary condition, which adds a forcing to push the vortices out.
(IBAMR does not provide a convective/advective boundary condition.) 
With this new configuration, the simulations of the snake profile resulted in a wake that looked physical, but a computed lift coefficient that was considerably different from our published study (Figure 6). 
Another deep dive in the literature led us to notice that a benchmark example described in a paper reporting on extensions to IBAMR^(5) was set up in an unexpected way: 
the no-slip condition is forced _inside_ the body, and not just on the boundary. 
As far as we could find, the publications using IBAMR are the only cases where interior points are constrained. 
Other papers using immersed boundary methods apply the constraint only on boundary points.
When we followed their example, our simulations with IBAMR were able to reproduce the lift enhancement at 35 degrees angle-of-attack, although with a slightly different value of average lift (<5% off). 
The successful result comes with a caveat, though. 
If we look at the time signature of the lift and drag coefficients, there is excellent agreement with our previous results for 30 degrees angle-of-attack (Re=2000). 
But at 35 degrees, the time signatures drift apart after about 40 time units (more than 150 thousand time steps). 
There is a marked drop in the (time varying) lift coefficient (Figure 7(b)), but because the average is calculated over a time range between 32 and 64 time units (a reasonable but arbitrary choice), the final numeric result is not far off our published study. 
Like in the previous case, using OpenFOAM, we make a judgement call that this result does indeed pass muster as a replication of our previous study. 