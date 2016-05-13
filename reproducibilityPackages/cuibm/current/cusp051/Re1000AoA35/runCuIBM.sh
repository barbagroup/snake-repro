# Run cuIBM from the branch `production-cusp-0.5.1`

CURRENT_DIR="$PWD"
cd $CUIBM_DIR
git checkout production-cusp-0.5.1
make all -j6
cd $CURRENT_DIR

$CUIBM_DIR/bin/cuIBM -caseFolder $PWD -deviceNumber 0 > summary.log &
