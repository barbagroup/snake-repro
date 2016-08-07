#!/bin/sh

# file: mergeForceCoefficientsFigures.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Merges the two .pdf into a single .pdf page.


INFILE1="ibamr_forceCoefficientsRe2000AoA30.pdf"
INFILE2="ibamr_forceCoefficientsRe2000AoA35.pdf"
OUTFILE="ibamr_forceCoefficientsRe2000.pdf"

pdfjam $INFILE1 $INFILE2 --nup 1x2 --outfile $OUTFILE

rm -f $INFILE1 $INFILE2

