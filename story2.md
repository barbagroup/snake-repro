## Story 2: You can hit snags with other researchers' codes

Open-source research software can often be poorly documented and unsupported, and on occasion it can even be an unreadable mess. 
But in this case, we are in luck.
IBAMR is a solid piece of software, the code is documented, and you can even get swift response from the authors via the topical online forum. 
The developers don't provide a user's manual, but they have plenty of examples within the code repository. 
Still, mastering other researchers' code is challenging and we hit a couple of snags that complicated the journey. 

IBAMR is described as "an adaptive and distributed-memory parallel implementation of the immersed boundary method."
The essence of the immersed boundary method is that the fluid is represented by a structured mesh, while the solid boundary is represented by its own, separate mesh that moves with the body. 
We speak of an Eulerian mesh for the fluid, and a Lagrangian mesh for the solid. 
The forces exerted by the fluid on the body, and vice versa, appear as an additional integral equation and interpolation schemes between the two meshes. 
The role of these is to make the fluid "stick" to the wall (no-slip boundary condition) and allow the body to feel aerodynamic forces (lift and drag). 
Our cuIBM code uses a variant called the immersed-boundary projection method \citep{taira2007}.
IBAMR is a library that provides different methods \citep{bhalla2013}, but despite the variations, we assumed it would work similarly.

We already know that boundary conditions at the outlet of the computational domain can be problematic. 
This is no different with immersed boundary methods. 
Our first attempt with IBAMR used a boundary condition at the outlet following their example for flow around a circular cylinder (this turned out to be a traction-free boundary condition). 
Unfortunately, it resulted in a spurious blockage of the wake vortices when they reach the domain boundary: strong vorticity rebounded from the artificial boundary and propagated back to the domain (Figure 5, top). 
Of course, this is unphysical and the result is unacceptable. 

In a conversation with the main developers on the online forum, they suggested a work-around: using "boundary stabilization," which adds a forcing to push the vortices out.
(IBAMR does not yet provide a convective/advective boundary condition.) 
With this new configuration, the simulations of the snake profile resulted in a wake that looked physical (Figure 5, bottom), but a computed lift coefficient that was considerably different from our published study (Figure 6). 
Another dive in the literature led us to notice that a benchmark example described in a paper reporting on extensions to IBAMR was set up in a way unexpected to us: 
the no-slip condition is forced _inside_ the body, and not just on the boundary. 
As far as we could find, the publications using IBAMR are the only cases where interior points are constrained. 
Other papers using immersed boundary methods apply the constraint only on boundary points.
When we followed their example, our simulations with IBAMR were able to reproduce the lift enhancement at 35 degrees angle-of-attack, although with a slightly different value of average lift (<5% off). 
The successful result comes with a caveat, though. 
If we look at the time signature of the lift and drag coefficients, there is excellent agreement with our previous results for 30 degrees angle-of-attack (Re=2000). 
But at 35 degrees, the time signatures drift apart after about 40 time units (more than 150 thousand time steps). 
There is a marked drop in the (time varying) lift coefficient (Figure 7(b)), but because the average is calculated over a time range between 32 and 64 time units (a reasonable but arbitrary choice), the final numeric result is not far off our published study. 
Like in the previous case, using OpenFOAM, we make a judgement call that this result does indeed pass muster as a replication of our previous study. 
