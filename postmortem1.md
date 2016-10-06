**Postmortem**. 
IcoFOAM solves the fluid equations using a finite-volume method in an unstructured grid, while our published study used an immersed boundary method in a stretched Cartesian grid. 
Comparing results obtained under such different conditions is a delicate operation. 
We made our best attempt at creating a fluid mesh for OpenFOAM that was of similar resolution near the body as we had used before. 
But unstructured grids are complex geometrical objects. 
Two unstructured meshes built with the same parameters will not be exactly the same, even. 
The mesh-generation procedures are not necessarily deterministic, and regularly produce bad triangles that need to be repaired. 
The complications of building a _good quality_ mesh is one of the reasons some prefer immersed boundary methods!
