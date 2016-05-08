#!/bin/sh

# file: mergeForceCoefficientsFigures.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Merges the 4 .pdf into a single .pdf page in a 2x2 display.


INFILE1="cuibm-cusp-0.5.1_forceCoefficientsRe1000AoA35.pdf"
INFILE2="cuibm-cusp-0.5.1_forceCoefficientsRe2000AoA30.pdf"
INFILE3="cuibm-revision86-cusp-0.4.0_forceCoefficientsRe2000AoA35.pdf"
INFILE4="cuibm-current-revision86_forceCoefficientsRe2000AoA35.pdf"
OUTFILE="cuibm_forceCoefficients.pdf"

pdfjam $INFILE1 $INFILE2 $INFILE3 $INFILE4 --nup 2x2 --outfile $OUTFILE

rm -f $INFILE1 $INFILE2 $INFILE3 $INFILE4

