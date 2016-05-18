#!/bin/sh

# file: mergeForceCoefficientsFigures.sh
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Merges the two .pdf into a single .pdf page.


INFILE1B="petibm011_forceCoefficientsRe2000AoA35.pdf"
INFILE1="petibm011_forceCoefficientsRe2000AoA35_2.pdf"
mv $INFILE1B $INFILE1
INFILE2="petibm011_forceCoefficientsRe2000AoA35CompareMarkers.pdf"
OUTFILE="petibm011_forceCoefficientsRe2000AoA35.pdf"

pdfjam $INFILE1 $INFILE2 --nup 1x2 --outfile $OUTFILE

rm -f $INFILE1 $INFILE2
