# Generates the information of the 2D structured Cartesian grid.
# The output file `domain.yaml` is saved in the present directory.
cp gridOptions_0.006.txt $CUIBM_DIR/scripts/grid/
python $CUIBM_DIR/scripts/grid/generateGrid.py \
	--input gridOptions_0.006.txt \
	--output domain.yaml
rm -rf $CUIBM_DIR/scripts/grid/gridOptions_0.006.txt

# Regularizes the body cross-section with spacing h=0.006 
# between two consecutive boundary points.
python $CUIBM_DIR/scripts/python/regularize.py \
	--ds 0.006 \
	--infile flyingSnake_0.004.bdy \
	--outfile flyingSnake

