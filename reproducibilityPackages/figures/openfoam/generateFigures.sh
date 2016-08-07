#!/bin/sh


python plotVorticity.py > plotVorticity.log

python plotPressure.py > plotPressure.log

python plotMeanForceCoefficientsVsAoACompareKrishnanEtAl2014.py \
  > plotMeanForceCoefficientsVsAoACompareKrishnanEtAl2014.log

python plotForceCoefficientsRe2000AoA30.py \
  > plotForceCoefficientsRe2000AoA30.log

python plotForceCoefficientsRe2000AoA35.py \
  > plotForceCoefficientsRe2000AoA35.log

./mergeForceCoefficientsFigure.sh