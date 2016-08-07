**Postmortem**. 
Making research codes open source is not enough for reproducibility: we must be meticulous in documenting every dependency and the versions used. 
Unfortunately, some of those dependencies will get stale over time, and might cease to be available or usable. 
Your application code may give the same answer with a different version of an external library, or it may not. 
In the case of unsteady fluid dynamics, the nonlinear nature of the equations combined with numerical non-reproducibility of iterative linear solvers (in parallel!) can change the results. 
