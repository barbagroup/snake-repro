**Postmortem**. 
Although PetIBM implements the same immersed-boundary method and was developed by the same research group, we were not able to fully replicate the previous findings. 
The aerodynamic lift on a snake section at 35 degrees angle-of-attack is a consequence of the near-wake vortices providing extra suction on the upper side of the body. 
When a vortex merger event changes the wake pattern, lift drops. 
Vortex merging is a fundamentally two-dimensional instability, so we expect that this problem won't trouble us in more realistic 3D simulations. 
But it is surprising that small changes---within the bounds of truncation error, roundoff error and algebraic errors---can trigger this instability, changing the flow appreciably. 
Even when the only difference between two equivalent simulations is the linear algebra library used, there can be challenges to reproducibility.
