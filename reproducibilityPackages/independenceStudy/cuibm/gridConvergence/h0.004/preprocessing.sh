cp gridOptions_0.004.txt $CUIBM_DIR/scripts/grid

python $CUIBM_DIR/scripts/grid/generateGrid.py \
	--input gridOptions_0.004.txt \
	--output domain.yaml

rm -rf $CUIBM_DIR/scripts/grid/gridOptions_0.004.txt
