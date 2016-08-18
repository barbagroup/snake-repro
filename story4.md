## Story 4: Different versions of your code, external libraries or even compilers may challenge reproducibility

In the span of about three years, we ran more than 100 simulations with OpenFOAM, IBAMR, and PetIBM, encountering about a dozen things that can go wrong. 
We replicated our previous scientific finding (enhanced lift at 35 degrees angle-of-attack for sufficiently large Reynolds number) in two out of three campaigns. 
Ironically, the case that did not replicate our findings was that of our own code re-write. 
The original code (cuIBM) and the re-write (PetIBM) use different linear algebra libraries, and it's unnerving to think this could change our results. 
This final story is about what happened when we went back to our _original_ code and tried to reproduce the published findings.

As we mentioned in the opening of this article, we adopted a set of practices years ago to make our research reproducible. 
The study published as "Lift and wakes of flying snakes" followed the guidance of the "Reproducibility PI Manifesto," 
which includes: 
(1) code developed under version control; 
(2) completed validation and verification, with report published on Figshare; 
(3) open data and figures for the main results of the paper on Figshare; 
(4) pre-print made available on arXiv; 
(5) code released under MIT License; 
(6) a Reproducibility statement in the paper.
Of course we expect to be able to reproduce our own results!

The first hurdle we faced is that, three years after we completed our previous study, we have updated our lab computers: 
new operating systems, new GPU devices, new external libraries. 
The code itself has been modified to implement new features. 
Happily, we have version control.
So, we set out to reproduce our results with cuIBM using (1) the "same"  old version of the code and (2) the current version. 
In both cases, we used identical input parameters (Lagrangian markers to discretize the geometry, grid parameters, flow conditions, and solver parameters). 
But the three-year-old simulations used a version of _Cusp_ (0.3.1) that is no longer compatible with the oldest CUDA version installed on our machines (5.0). 
Thus, we adapted "old" cuIBM to be compatible with the oldest version of _Cusp_ (0.4.0) that we can run. 
The case at angle-of-attack 35 degrees and Reynolds number 2000 now gave an appreciable difference compared with our previous study: 
the instantaneous force coefficients start to slowly drop after about 60 time units (Figure 11(c)). 
Now, this is _really_ the same code, with only a difference in the _version_ of the linear algebra library. 
Repeating the case with the most current version of cuIBM and the same version of _Cusp_ (0.4.0) leads to the same force signals, with a slight drop towards the end (Figure 11(d)). 
And the same is the case with the current version of cuIBM and a later version of _Cusp_ (0.5.1). 
The final _findings_ in these cases do not vary from our published work: there is, in fact, lift enhancement at 35 degrees angle-of-attack ... but the results match only because we calculate the average lift in a time interval between 32 and 64. 
Yet, the flow solution was affected by changing the version of a dependent library. 
(The revision history of _Cusp_ says that they refactored the smooth-aggregation solver between the two versions we are using.) 
The hardware was also different (a K20 GPU versus a C2070 in our older study), and the operating system, and the compiler. (Note that we always run with in double precision.) 
In an iterative linear solver, any of these things could be related to lack of floating-point reproducibility. 
And in unsteady fluid dynamics, small floating-point differences can add up over thousands of time steps to eventually trigger a flow instability (like vortex merging).
