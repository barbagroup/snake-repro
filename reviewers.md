## Editor

>The reviewers have made a number of useful comments that I feel will overall improve the manuscript. In particular, I direct the authors attention to comments about the stability of the problem, and there are some specific suggestions that the reviewers make that could improve clarity of language. Otherwise, I too agree with the reviewers that this paper is very important, and I look forward to seeing its impact on the field.

Some of the language in the section reporting our experience with IBAMR can be read as direct criticism towards the team that developed this library. 
We've heard from the IBAMR team that they object to our description.

In particular, the sentence "The published record is incomplete in this regard: we could find no explanation for it [the use of a solid body discretization instead of a boundary discretization] in any paper using IBAMR" was interpreted as an accusation that the papers deliberately leave out important details. 
This was not our intention in writing the text. 
We simply want to report our experience trying to learn how to use this code, and our mistakes in the process.

We modified the title of Story 2 to remove the word "trap" (see [change](https://www.authorea.com/users/99991/articles/121035/history/67b9906f2be1b199b8c5a8b338dd032447a3826d)) and polished our language in the section (see [change 1](https://www.authorea.com/users/99991/articles/121035/history/03d75aa05c452213a81b10e3c5f96cba9488bce6), [change 2](https://www.authorea.com/users/99991/articles/121035/history/71a9aa5f5077d68f467fc51f684b8aca1a52969e), and [change 3](https://www.authorea.com/users/99991/articles/121035/history/4ef0720312214ffee0b42eeb7cbd420d8ba6ec5e)).
We also fixed imprecisions in the description of the IBAMR library (see [change](https://www.authorea.com/users/99991/articles/121035/history/ac4cea22bc1b1c88ad22ccb86f60dbb59026668f)).

We also needed to correct the description of the outflow boundary conditions, which are not zero-gradient conditions, but traction-free conditions. 
This was our mistake in the description and we modified it during the revision (see [change](https://www.authorea.com/users/99991/articles/121035/history/84de3fed3cec9e24ef93d294de478de4e9ab099a)). 
And as the [discussion](http://lorenabarba.com/news/reproducible-and-replicable-cfd-its-harder-than-you-think/) following the post in our group web site shows, the IBAMR team is worried that readers could misinterpret Figure 5 as "a fundamental problem with the library." 
Thus, we edited Figure 5 of the manuscript to include a plot of the vorticity field when using a stabilized outlet boundary condition.

---

## Reviewer 1

> _Recommendation:_ Accept If Certain Minor Revisions Are Made
> 
> _Comments:_
> 
> I think the paper is great, but I would love for them to make it even better. This should be strongly encouraged. This should not preclude publication. Getting this work published is essential.
> Additional Questions:
> 
> * How relevant is this manuscript to the readers of this periodical? Please explain your rating in the Detailed Comments section. : Very Relevant
> 
> * To what extent is this manuscript relevant to readers around the world? : The manuscript is of interest to readers throughout the world
> 
> _1) Please summarize what you view as the key point(s) of the manuscript and the importance of the content to the readers of this periodical :_
> 
> * Current practice and software does not support fully reproducible work.
> * Aspects that should be relatively simple are anything but simple.
> * A variety of relatively benign issues actually hold us back from the state we need to be in.
> * Current practice falls very well short of the needs to be reproducible.
> 
> _2) Is the manuscript technically sound? Please explain your answer in the Detailed Comments section. :_ Yes
> 
> _3) What do you see as this manuscript's contribution to the literature in this field?:_ This paper is seminal on an essential aspect of modeling & simulation. Many of the issue are elucidated eloquently here. We need to publish results like this and our failure to do so is holding the field back.
> 
> _4) What do you see as the strongest aspect of this manuscript?:_ This is an important paper and topic. It absolutely needs to be published and read by the community at large. The message is important and it is delivered in a compelling and deeply engaging manner. The importance of publishing this sort of “negative” result cannot be overstated. Nonetheless a few weaknesses in the paper help to undermine the message enough that some corrective action is necessary. With a handful of changes this paper can become a real touchstone for the community to look to for paths for improving our computational practice. The suggestions below are far too expansive to be readily implemented, but are offered in the spirit of constructive criticism. I hope the authors can find the energy to move forward on some of these fronts and make an already excellent paper exceptional.
> 
> _5) What do you see as the weakest aspect of this manuscript?:_
> 
> 1- Perhaps the biggest issue to more completely address in the paper is the fundamental nature of the physical problem being solved. How well-posed is the problem, what sort of natural variability may be expected, and how reproducible are results intrinsically? One might look at a complementary study of vortex shedding off of a cylinder where the behavior is well-known. Are the results reproducible at very low Reynolds number? And do they cease being so as the Reynolds number increases, and if so at what value do the problems seen in the paper begin?

I read over Williamson (1996) again, looking for clues to frame the reply to this comment. 
It's true that bluff-body wakes are particularly complex flows—they involve three shear layers: the boundary layer, separating free shear layer, and the wake. 
During the revision of the manuscript, we added some notes about the shear layer instabilities involved in the problem investigated (see [change](https://www.authorea.com/users/99991/articles/121035/history/2789c0cfc477d3aad0a21af71d86cfe26e9160bf)).
Physically, we can talk about instabilities in all of these. 
The free shear layer, for example, is subject to Kelvin-Helmholtz instability (principally a 2D mechanism). 
In the case of the wake, von Karman showed in 1912 that vortex streets are unstable (although assuming infinite vortices and no body).

There are three vortex-shedding regimes: a "stable" periodic one for Re=40–150; a transition at Re=150–300, and an "irregular" regime at Re=300–10,000. We are squarely in the "irregular" regime.

Finally, Williamson cites work by Karniadakis and Triantafyllou (1992) suggesting that as Re increases "the wake velocity fluctuations indicate a cascade of period-doubling bifurcations, which create a chaotic state in the flow at around Re=500."

Yet, I don't think any of this is pertinent to the message of our paper. 
Yes our flow situation is complex. 
But you don't need a highly unsteady complex flow to be faced with challenges to reproducibility.

Take a simple saddle point in an ideal 2D flow. 
The dynamical system is linear and you can write down an analytical solution easily. 
But if you try to solve it numerically, it's going to be very sensitive to small errors. 
One initial condition right next to the stable manifold will come very close to the critical point, then go to infinity. 
Another initial condition very, very close, but on the other side of the manifold, will end up in minus infinity.

Any time you have exponential growth in the model, there will be huge challenges to numerical reproducibility. 
This is not a feature of complex vortical flows, in particular.

We can have long discussions about these issues, but it seems (to me) beyond the scope of our paper.

We already say that "highly unsteady fluid dynamics is a particularly tough application for reproducibility [...] In any application that has sufficient complexity, we should repeat simulations checking how robust they are to small variations." (p. 9).

"how reproducible are results intrinsically?" 
Well, there is no randomness in the model: the 2D Navier-Stokes equation should give deterministic results with sufficiently fine discretization, no?
WE DO, in fact, replicate the results (with OpenFOAM and IBAMR) eventually, so I think we've shown that there is no such intrinsic lack of reproducibility. It's just hard!

"at what value do the problems seen in the paper begin?" 
We computed with two different values of Re: 1000, and 2000. 
The difficulties appear at the higher value of Re. We're not going to repeat this painful process with values of Re in between! ... we already made hundreds of simulations, and this is not the point of the paper, right? 
We're trying to replicate a previously published finding at Re=1000 and 2000.

In summary, I think we can only stress the points we already make in the paper.

Regarding well-posedness—to be well posed, the initial-boundary value problem must have a unique solution and depend continuously on the data. 
With appropriate boundary conditions on pressure at infinity, the Navier-Stokes equations are well posed. 
(But, citing Nordstrom & Svard (2005): "…the exact form of the boundary conditions that lead to a well-posed problem is still an open question …")

It sounds like the referee may be hinting at a sudden change in behavior at a given Reynolds number. 
The part where a well-posed problem depends continuously on the data also means that "small" changes in the parameters cannot result in "large" changes in the solution.

But I still think it is not in the scope of this paper to engage in a discussion about this. 
We computed the solutions at two values of Re: 1000 and 2000. 
We can't speculate about a bifurcation at a value of Re, nor embark on hundreds more simulations to look at intermediate Reynolds numbers. 
The goal was to replicate previous results, and we did.

_References:_
* Williamson, Charles HK. "Vortex dynamics in the cylinder wake." Annual review of fluid mechanics 28.1 (1996): 477-539 DOI: 10.1146/annurev.fl.28.010196.002401.
* Karniadakis, G. E., & Triantafyllou, G. S. (1992). Three-dimensional dynamics and transition to turbulence in the wake of bluff objects. Journal of Fluid Mechanics, 238, 1-30.
* Nordström, J., & Svärd, M. (2005). Well-Posed Boundary Conditions for the Navier--Stokes Equations. SIAM Journal on Numerical Analysis, 43(3), 1231-1255.

> 2- I do not see any evidence of mesh convergence being conducted as part of the study. This seems to be a rather major and troubling shortcoming. We are given no evidence of whether any solution is remotely mesh independent or the degree of numerical error present in the solution. This is a major component of the proper practice in numerical modeling and simulation in this modern age all too often neglected in published works.

In this work, we are attempting to replicate the findings of a previous CFD paper (Krishnan et al., 2014), so three points to potentially make in the response: (1) evidence of grid convergence having been done in the previous work, Krishnan et al.; (2) since this is a replication study, we use the same mesh as in the previous result, i.e., the decision to use a mesh resolution is dictated by that criterion, rather than new mesh-convergence analysis; (3) despite the previous point, a posteriori mesh convergence can help explain when there are differences in the results.

Answer to (1) is that Krishnan et al. report mesh convergence: differences in the average lift coefficients are in the order of 2% at 35 deg AoA, and <0.1% at 30 deg.
We added a note about it during the revision of the manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/commits/e6d3c8beb4d49cc975f1016c8fd549dd0f646bee)).

PetIBM is the same method exactly as cuIBM, so the same mesh is used. 
The only algorithmic difference between the two codes is in the linear solver, so we checked that reducing the solver tolerance did not affect the solution (it did not).
We clarified this in the revised manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/commits/9cda5d9f84525ae31e5171598db4b3e1f08b2ef9)).

IBAMR, on the contrary, would require mesh convergence to be able to say that it’s meaningful to compare with the results of other codes. We refined the mesh with IBAMR, and the results are self-consistent, at least when looking at our chosen diagnostic, i.e., the average lift coefficient in a specified time range. Some differences, however, are apparent on the time signature of lift. With the mesh reported in the manuscript, we also decreased the solver tolerance, to make sure that discretization error is dominating and algebraic errors are not polluting the results. The results were also consistent when using a larger physical domain. — We’re confident saying that the simulations with IBAMR are mesh-converged and added a note about it the revised version of the paper (see [change](https://www.authorea.com/users/99991/articles/121035/commits/1d32cfe2dcb271363293b6d1ad103ed6949fa191)).

Although we were able to replicate, with IBAMR, the main finding of Krishnan et al. (2014), we would like to provide an additional result concerning the flow at Reynolds number 2000 when the bluff-body adopts a 35-degree angle-of-attack.

The manuscript from Bhalla et al. (2013) details the mathematical formulation implemented in the IBAMR library.
With IBAMR, we use a dynamic time-increment to advance in time based on a prescribed convective CFL constraint.
In their manuscript, Bhalla and co-workers mentioned that, otherwise noted, they used a CFL constraint of 0.3 in the examples reported.
One of their simulations concerns the two-dimensional flow around a fixed and rigid circular cylinder at Reynolds number 200. 
As no further information about the CFL constraint is provided, we assumed that they used a value of 0.3.
Another example deals with the locomotion of a two-dimensional eel at Reynolds number 5609.
Again, we could not find an updated value for the CFL constraint, thus guessed that a value of 0.3 was maintained to integrate the solution in time.

The Reynolds number of the eel example is of the same order of magnitude than the one in our flying-snake application; thus, we decided to use the same value for the CFL constraint.
We obtained good agreement in the time-averaged force coefficients between the simulations using IBAMR and the ones reported in Krishnan et al. (2014), especially at angles-of-attack 25 and 30 degrees.
Even if the coefficient at angle-of-attack 35 degrees is slightly smaller (-4.1%) than the one reported in Krishnan et al. (2014), the lift-curve exhibits a spike. 
Thus, we consider that we replicated with IBAMR the main finding of Krishnan et al. (2014).

However, digging into the input files of the eel application of Bhalla and co-workers (available on the GitHub repository of IBAMR), we saw that they used a CFL constraint of 0.1 (not 0.3).
Meanwhile, we also tried to use this CFL value to check the temporal convergence of our results.
When reducing the CFL constraint (from 0.3 to 0.1), we do not observe anymore a drop in the lift coefficient (as we did with a higher CFL), getting closer to the signature obtained with cuIBM by Krishnan and co-workers.
This new result does not modify the overall conclusions about IBAMR: we have been able to replicate the lift-enhancement reported in Krishnan et al. (2014).
However, it is important to mention that we obtained even closer time-averaged coefficients when reducing the CFL constraint.
During the revision stage of the manuscript: (1) we added this new IBAMR result with a lower CFL constraint in the text (see [change](https://www.authorea.com/users/99991/articles/121035/history/f5e706781966afe2ecf90e2084cfe52fbb861770)), (2) we added the time-averaged force coefficients to Figure 6, and (3) we added the lift and drag signature to Figure 7.

_References:_
* Bhalla, A. P. S., Bale, R., Griffith, B. E., & Patankar, N. A. (2013). A unified mathematical framework and an adaptive numerical method for fluid–structure interaction with rigid, deforming, and elastic bodies. Journal of Computational Physics, 250, 446-476.

> 3- There is not any significant investigation of the uncertainty from readily identifiable sources as part of the work. Does one basic code, or modeling aspect dominate the uncertainty and/or variation in the answer? This might go great lengths to differentiate each of the approaches taken in solving the problem.

> 4- UQ and V&V are never complete, but it can be adequate and fit to purpose. It is not clear that adequacy has been met in the case of the work presented in the paper. On the other hand UQ-V&V would not blunt many of the issues exposed in the tale being told.

> 5- One of the key reasons to write your own CFD code is the depth of expertise and understanding that it endows upon those that undertake the endeavor. Often those who uses a “canned” code simply possess are far too superficial understanding of how the simulation works, and where errors and biases enter into the results.

> 6- I wouldn’t use the term “discretization meshes” but rather a “mesh to use for discretization”.

We replaced the term "discretization meshes" by "mesh for discretization" during the revision of the manuscript (see [change 1](https://www.authorea.com/users/99991/articles/121035/history/5e085e05731df26080ade431d98bfc418032df75), [change 2](https://www.authorea.com/users/99991/articles/121035/history/91524d2960621bac5c7a43a3add13161c5bf78db), [change 3](https://www.authorea.com/users/99991/articles/121035/history/cda5ca8acf7486fe206ff67ccbc326e996d0c863)).

> 7- The whole affair with OpenFoam and boundary conditions is an object lesson in why you write a code in the first place.

> 8- I found the end of the section for story 1 to be troubling. This would seem to be a place where convergence testing might be very useful (not just mesh, but linear and nonlinear residuals too). It might be good to elaborate a bit more on the basic methods used by OpenFoam in the solution technique; I suspect the variation found is directly link to the solution techniques.

> 9- Tricks of the trade come directly from writing codes that work. If one doesn’t write the codes, these tricks start to look arbitrary and magical. Things like these tricks are often only justified by the fact they “work” and end up not being fully documented because they can’t be explained in a manner that isn’t slightly embarrassing.

> 10- The variation in the plots is another place where the lack of convergence testing in the results appears to be especially worrisome. The degree of variation seems to be unacceptable, and not entirely well explained.

> 11- The outflow boundary conditions issues were explored at length in the 1990’s by Phil Gresho and other researchers and documented in the Int. J Num. Meth. Fluids. It would seem to be a rather obvious source for gleaning greater insight on what is happening in this study.

In the revised version of the manuscript, we cite the report from Sani and Gresho (1994) to reflect on how choosing adequate outflow boundary conditions can be a frustrating exercise (see [change](https://www.authorea.com/users/99991/articles/121035/commits/fadc4f3e37a6a26046499483a62096c710bf53c2)).
_"We have made some attempts at shedding more light on the difficult and unresolved area of seeking good OBCs for incompressible flow simulations. It has been an exercise in frustration and we are not thrilled with the results obtained, even though they may still be useful to some researchers; thus we pass the baton."_ (Sani and Gresho, 1994)

_References:_
* Sani, R. L., & Gresho, P. M. (1994). Résumé and remarks on the open boundary condition minisymposium. International Journal for Numerical Methods in Fluids, 18(10), 983-1008.

> 12- The linear algebra episode is a bit troubling and would seem to indicate some rather fundamental issues with the solver discretization. There may be a discrete violation of the Fredholm integral that renders the CG solver problematic. This might be a side effect of the discrete system being corrupted rather than a shortcoming of the solver itself. For properly formed symmetric systems, CG is vastly more robust and cost effective than BiCGstab!

> 13- The whole episode with the libraries seems to indicate that the problem you are solving is itself unstable. This is another place where the lack of convergence testing and fundamental UQ may have a serious impact on the story. What level of fundamental physically reasonable variability can be expected in this problem? I suspect the degree of variability is actually quite large and therefore the problem may not lend itself to strict reproducibility. Instead there is a probabilistic framework for reproducibility that may make far more sense in the long run. The thing to reproduce may be statistical properties of the solution rather than a well-posed and unique initial value problem.

We think it would have been too long to reproduce statistical properties.
To have enough data to compute the time-averaged for coefficients, we computed the solution up to 80 non-dimensional time-units.
The simulations reported in the manuscript last between one and three days (using one GPU with cuIBM and up to 32 CPU cores with the other software).

> 14- Computations actually began in the 1940’s in Los Alamos (during WWII). The first punched cards were used for the data flow of the calculation long before the code itself was on cards (details can be found on the LANL web site). Tape actually preceded cards for the written program, and the earlier machines were programmed by rewiring the computer itself with cable plugs (a couple of Los Alamos reports from the late-1940’s contain wiring diagrams).

In the first version of the manuscript, we mentioned that the origins of CFD in the Los Alamos Laboratory took place in the 1950's.
As pointed out by the reviewer, the origins of CFD date back to the 1940's.
The pleasant-to-read and informative paper by Metropolis and Nelson (1982) relates the transition from hand-computing to punched-card computation, and then electronic computing.
The Los Alamos laboratory ordered its first punched-card machines from IBM. 
During war-time, the research conducted was so sensitive that IBM was not allowed to send a crew to install the machines at the laboratory:
_"Through our army connections, we asked IBM for the name of its best maintenance man drafted into the U.S. Army; that man, John Johnston, was requisitioned."_
At the beginning, the boxes of punched cards were difficult to "share" not only because of their largeness, but also because everything was kept secret.
Note that the punched-card machines were used for implosion simulation that required integrating a two-dimensional partial differential equation.

In the revised version of the manuscript, we corrected the timing in the sentence related to the beginning of CFD at the Los Alamos Laboratory and added a reference to Metropolis and Nelson (1982) (see [change](https://www.authorea.com/users/99991/articles/121035/history/488aae197712bf88428e91bf91b9d834b41211ff)).

_References:_
* Metropolis, N., & Nelson, E. C. (1982). Early Computing at Los Alamos. Annals of the History of Computing, 4(4), 348-357.

> 15- Overall the references are too Spartan and need to be beefed up to reflect better scholarship.

We added several citations to our manuscript, based on the suggestions from the three reviewers.

> 16- The discussion around the failings of the published literature is quite good. It might be buoyed by some examples where the publication of negative results have had a disproportionately positive impact on the community. A couple of good examples are the paper by Quirk or Ioannidis included below.

Quirk (1997) would be an excellent citation in our manuscript concerning the publication of negative results. Quirk addresses some issues related to current (at that time) Godunov-type methods implemented in Riemann solvers. The author offers a "catalogue" of possible failures encountered with Godunov schemes, one of them being unreported prior this publication. In addition, Quirk proposes a remedy to fix those failings.
We now cite Quirk (1997) in the revised manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/commits/8439be341f34dbaff4a56c3b289bb9f529d85ec5)).

In addition to that, we added a reference to Ioannidis (2005) when talking about current publication are biased towards positive results (see [change](https://www.authorea.com/users/99991/articles/121035/history/a5c40a319e68a9f457825c39cbe9e264f86ecbcd)).

_References:_
* Quirk, J. J. (1997). A contribution to the great Riemann solver debate. In Upwind and High-Resolution Schemes (pp. 550-569). Springer Berlin Heidelberg.
* Ioannidis, J. P. (2005). Why most published research findings are false. PLoS Med, 2(8), e124.

> 
> _References_
> 
> Oberkampf, William L., and Christopher J. Roy. Verification and validation in scientific computing. Cambridge University Press, 2010.
> 
> Gresho, Philip M., and Robert L. Sani. "On pressure boundary conditions for the incompressible Navier‐Stokes equations." International Journal for Numerical Methods in Fluids 7.10 (1987): 1111-1145.
> 
> Sani, Robert L., and Philip M. Gresho. "Résumé and remarks on the open boundary condition minisymposium." International Journal for Numerical Methods in Fluids 18.10 (1994): 983-1008.
> 
> Metropolis, Nicholas, and Eldred C. Nelson. "Early Computing at Los Alamos." Annals of the History of Computing 4.4 (1982): 348-357.
> 
> Mattsson, Ann E., and William J. Rider. "Artificial viscosity: back to the basics." International Journal for Numerical Methods in Fluids 77.7 (2015): 400-417.
> 
> Quirk, James J. "A contribution to the great Riemann solver debate." Upwind and High-Resolution Schemes. Springer Berlin Heidelberg, 1997. 550-569.
> 
> Ioannidis, John PA. "Why most published research findings are false." PLoS Med 2.8 (2005): e124.
> 
> 1. Does the manuscript contain title, abstract, and/or keywords?: Yes
> 
> 2. Are the title, abstract, and keywords appropriate? Please elaborate in the Detailed Comments section.: Yes
> 
> 3. Does the manuscript contain sufficient and appropriate references (maximum 12-unless the article is a survey or tutorial in scope)? Please elaborate in the Detailed Comments section.: Important references are missing; more references are needed
> 
> 4. Does the introduction clearly state a valid thesis? Please explain your answer in the Detailed Comments section.: Yes
> 
> 5. How would you rate the organization of the manuscript? Please elaborate in the Detailed Comments section.: Satisfactory
> 
> 6. Is the manuscript focused? Please elaborate in the Detailed Comments section.: Satisfactory
> 
> 7. Is the length of the manuscript appropriate for the topic? Please elaborate in the Detailed Comments section.: Could be improved
> 
> 8. Please rate and comment on the readability of this manuscript in the Detailed Comments section.: Easy to read
> 
> 9. Please rate and comment on the timeliness and long term interest of this manuscript to CiSE readers in the Detailed Comments section. Select all that apply.: Topic and content are likely to be of growing interest to CiSE readers over the next 12 months
> 
> Please rate the manuscript. Explain your choice in the Detailed Comments section.: Excellent

---

## Reviewer 2

> _Recommendation:_ Accept If Certain Minor Revisions Are Made
> 
> _Comments:_
> This is an interesting paper that raises a number of important issues while also telling a good story about the authors' experiences and frustrations, in a manner that is enjoyable to read as well as highly informative. So I think it will make a very good article for CiSE.
> 
> However, to some extent I think the authors conflate issues in a way that might be confusing or misleading for some readers.
> 
> The unsteady flow problem considered here is highly sensitive to perturbations, and the determination of a quantity such as the optimal angle of attack seems to be ill-conditioned. This means that small changes in the method, grid resolution, boundary conditions, etc. can have a significant effect on the results obtained. This is a classic issue in numerical analysis and fluid dynamics that has been a core subject of study for decades, and in some sense has little to do with the recent surge of interest in "reproducible research". Many of the issues raised in the paper regarding this sensitivity and the ways in which different numerical methods and implementations react to it are essential for anyone to be aware of who works on this type of problem, and should properly be considered as part of any original publication in this field, not only as an issue that arises when reproducing past work. I am sure the authors are aware of this, but this may not come across to readers from other fields. References are made to the extreme sensitivity of this particular CFD problem, e.g. in in the postmorten on p. 7 and the lessons learned on p. 9, but I think it would be valuable to discuss this in the introduction to the article.

We added some notes in the introduction of the manuscript about the nature of the flow investigated here and why it is particularly challenging to simulate it (see [change](https://www.authorea.com/users/99991/articles/121035/history/2789c0cfc477d3aad0a21af71d86cfe26e9160bf)).

> My fear with the current presentation is that readers might get the impression that reproducibility in CFD is hopeless so they may as well not try, whereas the real lessons I think are that (a) this particular type of problem has sensitivity issues that one should be aware of before publishing any results -- don't believe what comes out of one code at one grid resolution without doing careful sensitivity studies and (b) this problem adds additional complication to trying to make ones own work reproducible (even by the same group with the same code later) due to changes in hardware or software dependencies.
> 
> And I think it should also be pointed out that (c) not all CFD problems are nearly this sensitive -- for other types of flow many of these problems would not arise and it would be much easier to reproduce/replicate results, and (d) even for this sensitive problem, it was invaluable that the original code was kept under version control and properly archive since this greatly facilitated this replication study, and allowed the determination of exactly what differences in software led to differences in newer results compared to those originally published. This behavior should be encouraged in the interest of advancing science.

In response to this comment by the referee, we do think that most CFD problems of interest today are unsteady and present challenges like the ones we illustrate in the manuscript. 
Flow situations that present no challenge—e.g., laminar, steady, simple geometry—are routine and not very interesting!

Even for steady flow, if the Reynolds number is high, the replication challenge is steep. 
For example, the AIAA Drag Prediction Workshop has been ongoing since 2001, demonstrating wide differences between results with different (yet trusted) codes. 
(We added to the manuscript a mention and citation for the AIAA effort.)

We have added more discussion about the physical flow situation, mentioning that it is subject to various instabilities. 
Numerous flow situations of interest have these instabilities, and we agree with the referee that they add extra challenges to replication. 
But this is quite often the case in CFD. We don't see that it's possible to dissociate the sensitivity of the flow physics with the reproducibility challenges that they bring. 
The message of the paper is that replication and reproducibility in CFD can be hard—unless one has a very uninteresting flow.

> It is also commendable that the code to support this study is all available on GitHub, although I have not attempted to repeat the experiments myself.
> 
> _Additional Questions:_
> 
> How relevant is this manuscript to the readers of this periodical? Please explain your rating in the Detailed Comments section. : Very Relevant
> 
> To what extent is this manuscript relevant to readers around the world? : The manuscript is of interest to readers throughout the world
> 
> _1) Please summarize what you view as the key point(s) of the manuscript and the importance of the content to the readers of this periodical. :_ Points out many difficulties in trying to replicate/reproduce previous results obtained with computational fluid dynamics, both using the same code as the original study and using other software. There are many illustrations of pitfalls that can arise. These observations should be of interest to anyone doing CFD in a similar unsteady regime, whether or not they are interested in "reproducible research".
> 
> _2) Is the manuscript technically sound? Please explain your answer in the Detailed Comments section. :_ Yes
> 
> _3) What do you see as this manuscript's contribution to the literature in this field?:_ It contains an excellent summary of issues that are illustrated through a real-world example, and well described.
> 
> _4) What do you see as the strongest aspect of this manuscript?:_ It raises awareness of many difficulties in doing such research and obtaining results one can trust, as well as difficulties in trying to replicate experiments years later, even with the same software.
> 
> _5) What do you see as the weakest aspect of this manuscript?:_ As described further in m y detailed report, I think it should be pointed out that this unsteady problem is highly ill-conditioned and that not all CFD problems are so sensitive, and also that the issues raised in this paper go beyond "reproducible research" to how one properly does research on such problems.
> 
>     1. Does the manuscript contain title, abstract, and/or keywords?: Yes
> 
>     2. Are the title, abstract, and keywords appropriate? Please elaborate in the Detailed Comments section.: Yes
> 
>     3. Does the manuscript contain sufficient and appropriate references (maximum 12-unless the article is a survey or tutorial in scope)? Please elaborate in the Detailed Comments section.: References are sufficient and appropriate
> 
>     4. Does the introduction clearly state a valid thesis? Please explain your answer in the Detailed Comments section.: Could be improved
> 
>     5. How would you rate the organization of the manuscript? Please elaborate in the Detailed Comments section.: Satisfactory
> 
>     6. Is the manuscript focused? Please elaborate in the Detailed Comments section.: Satisfactory
> 
>     7. Is the length of the manuscript appropriate for the topic? Please elaborate in the Detailed Comments section.: Satisfactory
> 
>     8. Please rate and comment on the readability of this manuscript in the Detailed Comments section.: Easy to read
> 
>     9. Please rate and comment on the timeliness and long term interest of this manuscript to CiSE readers in the Detailed Comments section. Select all that apply.: Topic and content are of immediate and continuing interest to CiSE readers
> 
> Please rate the manuscript. Explain your choice in the Detailed Comments section.: Excellent

---

## Reviewer 3

> _Recommendation:_ Accept If Certain Minor Revisions Are Made
> 
> _Comments:_
> ... below is my review of the paper "Reproducible and
> replicable CFD: It's harder than you think". This is a nice paper, and
> will be a good contribution to the literature. I have the following
> remarks for revising the manuscript:
> 
> 1- A little more introduction to the physics in nature, setup of the
> simulation methodology, and findings of the main problem (lift of a
> flying snake) should be discussed, instead of just referencing the
> paper of the study

We added some text about the physics involved in the type of flow studied here (see [change](https://www.authorea.com/users/99991/articles/121035/history/2789c0cfc477d3aad0a21af71d86cfe26e9160bf) in the manuscript).

Findings of the previous study (Krishnan et al., 2014) are discussed briefly in the introduction. 
(Sentence beginning _"The main finding of our study on wakes of flying snakes was ... "_). 
We added a citation to the experimental study that revealed the enhanced lift (see [change](https://www.authorea.com/users/99991/articles/121035/history/b2dfc8fe64c62752bd5e9444f814cfca10fef468)) and a sentence about the mechanism behind it (see [change](https://www.authorea.com/users/99991/articles/121035/history/3f7f7a255204ef6f7b8a1ff4873bf6d42cad0b15)).

The manuscript is already past the maximum word limit, and so we must count on the interested reader consulting the original study for details of the simulation methodology and the explanation of the lift-enhancement mechanism.
We think that the main points of this paper can be followed without more details about the previous study.

> 2- There should be some discussion about other efforts to compare
> different codes on the same problem. Some of the ones that come to
> mind are:
> 
>     * The Santa Barbara Cluster Comparison Project: 
>     https://arxiv.org/abs/astro-ph/9906160
> 
>     * The Alpha Group Collaboration: 
>     http://scitation.aip.org/content/aip/journal/pof2/16/5/10.1063/1.1688328
> 
>     * Disk-planet interaction comparisons: 
>     http://www.tat.physik.uni-tuebingen.de/~kley/publ/paper/valborro.pdf
> 
>     Although many of these are compressible (but not all, e.g. for the
>     alpha group), they share the level of differences and in-depth
>     knowledge of the code needed as reported in this paper.

We added some comments about previous efforts to compare multiple CFD codes (see [change 1](https://www.authorea.com/users/99991/articles/121035/commits/26cdea37a0d473be4e828dfdeca8b3e1b653ca95), [change 2](https://www.authorea.com/users/99991/articles/121035/commits/38320719c93af03ec1c5b31fd3b92ab3433e3850), and [change 3](https://www.authorea.com/users/99991/articles/121035/commits/c7e19b78e0aabb65a6376a01b53aff50eb92883a) in the manuscript).

> 3- In "Story 1", the authors use the term "blow up" -- this should be
> clarified

The term "blow up" used in Story 1 of the manuscript means a degeneration of the numerical solution leading to a crash (sudden halt) of the simulation.
We clarified the term in the Story 1 (see [change](https://www.authorea.com/users/99991/articles/121035/history/2a6151f645d270ebc4cc2f3756515eef97135334) in the manuscript).

> 4- In "Story 1", the authors devote a few paragraphs discussing mesh
> quality -- figures showing these meshes need to be included in the
> paper -- it will really help the discussion.

We added plots of the mesh generated with GMSH and SnappyHexMesh in the supplementary materials.
Details about the mesh generation are also available in the supplementary materials.
We changed the text in the manuscript to guide the reader to the supplementary materials to look at the meshes (see [change](https://www.authorea.com/users/99991/articles/121035/history/5e745d011aecfa6d8a891439439350ffc8ea5077) in the manuscript).

> 5- "advective" boundary conditions should be defined -- what is the
> mathematical definition of this?

We added an explanation of an advective boundary condition in the manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/history/14e557a1f9e696305e0ff749fc13954046a772f3)).

> 6- In this discussion of the hardware changes from 3 years ago to
> present, it was noted that the GPUs changed -- were they all doing
> double precision floating point? A note about this should be
> added.

Krishnan et al. (2014) used a NVidia Tesla C2070 GPU to compute the numerical solution with cuIBM while we used a NVidia Tesla K20 in the present work.
Both GPUs were used with double precision floating point.
We added a note about it in the manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/history/22a5643db83c6d844163991286092b3a8f89540d)).
 
> 7- In the final paragraph, the authors advocate for continued release
> of CFD codes, and list some reason for not sharing. An important
> one that readers should be aware of is export control (especially
> for radiation hydrodynamics codes).

We added a mention about export control as another reason for not sharing code (see [change](https://www.authorea.com/users/99991/articles/121035/commits/247885c1ed73fccc1da4535f77831704a4bfd539) in the manuscript).

> 8- The authors discuss issues with the the software stack changing
> from three years ago to present. There are some efforts to help
> capture the state of the machine (OS, compilers, libraries, etc.)
> using Docker containers. The authors should comment on these efforts
> and whether they would have helped with their workflow.

Our in-house software, cuIBM and PetIBM, use GitHub's wiki or README markdown files to guide the user during the building stage.
Software documentation is rarely perfect.
Incomplete documentation makes it difficult for the user to build and use an application and a nightmare when trying to reproduce a study.
Docker appears as an attractive open-source tool to adopt a reproducible workflow (e.g., see Boettiger, 2015, and Chamberlain and Schommer, 2014).
Docker allows a developer to deploy an application (and all its dependencies) in a container, a lightweight virtual machine--a container does not create a whole virtual operating system but used the Linux kernel on the system it is running on.
Thus, Docker ensures that a software will run the same way on any Linux machine.
It would have been easier for us to reproduce the results from our previous study if a Docker container had been created in first instance, ensuring the computational environment to be identical.
We added a mention to Docker containers in our manuscript (see [change](https://www.authorea.com/users/99991/articles/121035/history/3e29be7e68ec24d7c1cedbf98ac5011c68fe528c)).
However, we note that Docker containers were not available when the first study was in progress.

_References:_
* Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.
* Chamberlain, R., & Schommer, J. (2014). Using Docker to support reproducible research. DOI: http://dx. doi. org/10.6084/m9. figshare, 1101910.

> _Additional Questions:_
> 
> * How relevant is this manuscript to the readers of this periodical? Please explain your rating in the Detailed Comments section. : Very Relevant
> 
> * To what extent is this manuscript relevant to readers around the world? : The manuscript is of interest to readers throughout the world
> 
> _1) Please summarize what you view as the key point(s) of the manuscript and the importance of the content to the readers of this periodical. :_ This provides a nice case study on how challenging reproducible research is to investigators, and will be common to all the readers.
> 
> _2) Is the manuscript technically sound? Please explain your answer in the Detailed Comments section. :_ Yes
> 
> _3) What do you see as this manuscript's contribution to the literature in this field?:_ This is a broad description of the problems one encounters with reproducibility.
> 
> _4) What do you see as the strongest aspect of this manuscript?:_ The lengthy personal experience that the authors convey.
> 
> _5) What do you see as the weakest aspect of this manuscript?:_ It would benefit from discussion on other attempts on reproducibility in CFD reported in the field.
> 
>     1. Does the manuscript contain title, abstract, and/or keywords?: Yes
> 
>     2. Are the title, abstract, and keywords appropriate? Please elaborate in the Detailed Comments section.: Yes
> 
>     3. Does the manuscript contain sufficient and appropriate references (maximum 12-unless the article is a survey or tutorial in scope)? Please elaborate in the Detailed Comments section.: References are sufficient and appropriate
> 
>     4. Does the introduction clearly state a valid thesis? Please explain your answer in the Detailed Comments section.: Yes
> 
>     5. How would you rate the organization of the manuscript? Please elaborate in the Detailed Comments section.: Could be improved
> 
>     6. Is the manuscript focused? Please elaborate in the Detailed Comments section.: Satisfactory
> 
>     7. Is the length of the manuscript appropriate for the topic? Please elaborate in the Detailed Comments section.: Satisfactory
> 
>     8. Please rate and comment on the readability of this manuscript in the Detailed Comments section.: Easy to read
> 
>     9. Please rate and comment on the timeliness and long term interest of this manuscript to CiSE readers in the Detailed Comments section. Select all that apply.: Topic and content are of immediate and continuing interest to CiSE readers
> 
> Please rate the manuscript. Explain your choice in the Detailed Comments section.: Excellent