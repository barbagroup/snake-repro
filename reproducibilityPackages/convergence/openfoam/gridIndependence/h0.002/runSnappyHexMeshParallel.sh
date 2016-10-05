#!/bin/sh

# Generates a mesh with SnappyHexMesh using N processors.


N=4

# source tool run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

# clean previous mesh
rm -rf log.mesh && mkdir log.mesh
rm -f constant/triSurface/*.eMesh
rm -rf constant/extendedFeatureEdgeMesh
find constant/polyMesh -type f \! -name 'blockMeshDict' -delete
mv 0 0.backup && mkdir 0

# create base mesh
runApplication blockMesh
mv log.blockMesh log.mesh

# create edge mesh for boxes
runApplication surfaceFeatureExtract
mv log.surfaceFeatureExtract log.mesh

# decompose base mesh
cp system/decomposeParDict_resources/decomposeParDict.hierarchical system/decomposeParDict
runApplication decomposePar
mv log.decomposePar log.mesh
runApplication renumberMesh -overwrite
mv log.renumberMesh log.mesh

# create castellated mesh (using N processors)
cp system/snappyHexMeshDict_resources/snappyHexMeshDict.castellated system/snappyHexMeshDict
# runParallel snappyHexMesh $N -overwrite -parallel
MPIRUN="/opt/OpenFOAM/ThirdParty-2.2.2/platforms/linux64Gcc/openmpi-1.6.3/bin/mpirun"
$MPIRUN -np $N snappyHexMesh -overwrite -parallel > log.snappyHexMesh
mv log.snappyHexMesh log.mesh/log.snappyHexMesh.castellated
rm -r system/decomposeParDict system/snappyHexMeshDict

# reconstruct mesh
runApplication reconstructParMesh -mergeTol 1.0E-06 -constant
mv log.reconstructParMesh log.mesh
rm -rf processor*

# flatten front and back planes of a 2d Cartesian mesh
runApplication flattenMesh
mv log.flattenMesh log.mesh

# extrude mesh in third direction
runApplication extrudeMesh
mv log.extrudeMesh log.mesh

# clean constant/polyMesh directory
cd constant/polyMesh
rm -f cellLevel level0Edge pointLevel refinementHistory surfaceIndex
cd ../..

# snap castellated mesh on surface
cp system/snappyHexMeshDict_resources/snappyHexMeshDict.snapped system/snappyHexMeshDict
runApplication snappyHexMesh -overwrite
mv log.snappyHexMesh log.mesh/log.snappyHexMesh.snapped
rm -f system/snappyHexMeshDict

# create patches
runApplication createPatch -overwrite
mv log.createPatch log.mesh

# check mesh quality
runApplication checkMesh
mv log.checkMesh log.mesh

# restore initial conditions folder
rm -rf 0 && mv 0.backup 0
