"""
Plots the instantaneous force coefficients and compares with the ones obtained
for a simulation using a bigger CFL constraint (cfl=0.3).
Here, we use a CFL value of 0.3.
All other parameters remain unchanged.

The script generates the figure `forceCoefficientsCompareCFL.png`
saved in the directory of the present script.
"""

import os
import yaml
import argparse

from matplotlib import pyplot

import snake
from snake.ibamr.simulation import IBAMRSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


directory = os.path.join(os.path.dirname(__file__),
                         'cfl0.1')
simulation = IBAMRSimulation(description='cfl=0.1',
                             directory=directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])

directory = os.path.join(os.path.dirname(__file__),
                         'cfl0.3')
loose = IBAMRSimulation(description='cfl=0.3',
                        directory=directory)
loose.read_forces()
loose.get_mean_forces(limits=[32.0, 64.0])

dataframe = simulation.create_dataframe_forces(display_coefficients=True,
                                               coefficient=-2.0)
dataframe2 = loose.create_dataframe_forces(display_coefficients=True,
                                           coefficient=-2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

# Plots the instantaneous force coefficients
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, -2.0*simulation.forces[0].values,
        label='$C_d$ ($CFL=0.1$)',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(loose.forces[0].times, -2.0*loose.forces[0].values,
        label='$C_d$ ($CFL=0.3$)',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, -2.0*simulation.forces[1].values,
        label='$C_l$ ($CFL=0.1$)',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(loose.forces[1].times, -2.0*loose.forces[1].values,
        label='$C_l$ ($CFL=0.3$)',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([0.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 12})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsCompareCFL.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
