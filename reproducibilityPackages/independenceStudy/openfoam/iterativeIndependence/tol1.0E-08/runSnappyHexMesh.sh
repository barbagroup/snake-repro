#!/bin/sh

# source tool run functions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

rm -rf log.mesh && mkdir log.mesh
rm -f constant/triSurface/*.eMesh
rm -rf constant/extendedFeatureEdgeMesh
find constant/polyMesh -type f \! -name 'blockMeshDict' -delete

# create base mesh
runApplication blockMesh
mv log.blockMesh log.mesh

# create edge mesh for boxes
runApplication surfaceFeatureExtract
mv log.surfaceFeatureExtract log.mesh

# create castellated mesh
cp system/snappyHexMeshDict_resources/snappyHexMeshDict.castellated system/snappyHexMeshDict
runApplication snappyHexMesh -overwrite
mv log.snappyHexMesh log.mesh/log.snappyHexMesh.castellated
rm -f system/snappyHexMeshDict

# flatten front and back planes of a 2d Cartesian mesh
runApplication flattenMesh
mv log.flattenMesh log.mesh

# extrude mesh in third direction
runApplication extrudeMesh
mv log.extrudeMesh log.mesh

# clean constant/polyMesh directory
cd constant/polyMesh
rm -rf cellLevel level0Edge pointLevel refinementHistory surfaceIndex
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
