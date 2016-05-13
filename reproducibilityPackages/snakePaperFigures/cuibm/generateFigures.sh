#!/bin/sh


python plotForceCoefficientsRe2000AoA30.py \
  > plotForceCoefficientsRe2000AoA30.log

python plotForceCoefficientsRe1000AoA35.py \
  > plotForceCoefficientsRe1000AoA35.log

python plotForceCoefficientsRe2000AoA35Revision86Cusp040.py \
  > plotForceCoefficientsRe2000AoA35Revision86Cusp040.log

python plotForceCoefficientsRe2000AoA35CurrentRevision86.py \
  > plotForceCoefficientsRe2000AoA35CurrentRevision86.log

./mergeForceCoefficientsFigure.sh