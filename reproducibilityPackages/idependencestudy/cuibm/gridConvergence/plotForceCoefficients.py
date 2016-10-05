"""
Plots the instantaneous force coefficients obtained on three systematically 
refined grids in the uniform region (h=0.006, 0.004, and 0.00267).
The grid is stretched outside the uniform region to the external boundaries with
a constant ratio of 1.01.
We use absolute tolerances of 1.0E-16 and 1.0E-06 as exit criterion for the 
velocity and Poisson solvers, respectively.
"""

import os
import warnings

import numpy
from matplotlib import pyplot

import snake
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


cases = []
fx, fy = [], []
resolutions = ['h=0.00267', 'h=0.004', 'h=0.006']
time_limits = (20.0, 28.0)

for resolution in resolutions:
  case = CuIBMSimulation(directory=os.path.join(os.path.dirname(__file__),
                                                resolution.replace('=', '')),
                         description=resolution)
  case.read_forces()
  case.get_mean_forces(limits=time_limits)
  fx.append(case.forces[0].mean['value'])
  fy.append(case.forces[1].mean['value'])
  cases.append(case)

# Calculates the observed order of convergence for the time-averaged force
# coefficients.
ratio = 1.5
order = numpy.log((fx[2]-fx[1])/(fx[1]-fx[0]))/numpy.log(ratio)
print(order)
order = numpy.log((fy[2]-fy[1])/(fy[1]-fy[0]))/numpy.log(ratio)
print(order)

# Plots the instantaneous force coefficients obtained with different meshes.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
colors = ('#377eb8', '#ff7f00', '#990026', '#002699', '#739900', '#CC0099')
for i, case in enumerate(cases):
  ax.plot(case.forces[0].times, 2.0*case.forces[0].values,
          label='$C_d$ - ${}$'.format(resolutions[i]),
          color=colors[2*i],
          linestyle='-', linewidth=1,
          zorder=10+i)
for i, case in enumerate(cases):
  ax.plot(case.forces[1].times, 2.0*case.forces[1].values,
          label='$C_l$ - ${}$'.format(resolutions[i]),
          color=colors[2*i+1],
          linestyle='-', linewidth=1,
          zorder=10+i)
ax.axis([0.0, 30.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 10})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficients.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)

# Plots the instantaneous lift coefficients over a smaller time-range.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
colors = ('#377eb8', '#ff7f00', '#990026', '#002699', '#739900', '#CC0099')
for i, case in enumerate(cases):
  ax.plot(case.forces[1].times, 2.0*case.forces[1].values,
          label='$C_l$ - ${}$'.format(resolutions[i]),
          color=colors[2*i+1],
          linestyle='-', linewidth=1,
          zorder=10+i)
ax.axis([20.0, 30.0, 1.5, 3.5])
ax.legend(ncol=1, loc='upper right', prop={'size': 10})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsZoom.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
