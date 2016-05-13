#!/bin/sh


python plotVorticity.py > plotVorticity.log

python plotMeanForceCoefficientsVsAoACompareKrishnanEtAl2014.py \
  > plotMeanForceCoefficientsVsAoACompareKrishnanEtAl2014.log

python plotForceCoefficientsRe2000AoA35.py \
  > plotForceCoefficientsRe2000AoA35.log

python plotForceCoefficientsRe2000AoA35CompareMarkers.py \
  > plotForceCoefficientsRe2000AoA35CompareMarkers.log

./mergeForceCoefficientsFigure.sh