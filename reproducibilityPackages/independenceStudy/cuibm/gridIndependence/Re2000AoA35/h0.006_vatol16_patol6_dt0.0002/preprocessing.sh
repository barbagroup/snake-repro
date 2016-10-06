cp gridOptions_0.006.txt $CUIBM_DIR/scripts/grid

python $CUIBM_DIR/scripts/grid/generateGrid.py \
	--input gridOptions_0.006.txt \
	--output domain.yaml

rm -rf $CUIBM_DIR/scripts/grid/gridOptions_0.006.txt

python $CUIBM_DIR/scripts/python/regularize.py \
	--ds 0.006 \
	--infile flyingSnake_0.004.bdy \
	--outfile flyingSnake
