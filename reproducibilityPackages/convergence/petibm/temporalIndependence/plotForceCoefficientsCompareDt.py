"""
Plots the instantaneous force coefficients and compares with the ones obtained
for a simulation using a bigger time-increment (dt=0.0004).
Here, the time-increment is set to dt=0.0002.
All other parameters remain unchanged.

The script generates the figure `forceCoefficientsCompareDt.png`
saved in the current working directory.
"""

import os
import yaml
import argparse

from matplotlib import pyplot

import snake
from snake.petibm.simulation import PetIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


directory = os.path.join(os.path.dirname(__file__), 'dt0.0002')
simulation = PetIBMSimulation(description='dt=0.0002',
                              directory=directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])

directory = os.path.join(os.path.dirname(__file__), 'dt0.0004')
loose = PetIBMSimulation(description='dt=0.0004',
                         directory=directory)
loose.read_forces()
loose.get_mean_forces(limits=[32.0, 64.0])

dataframe = simulation.create_dataframe_forces(display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = loose.create_dataframe_forces(display_coefficients=True,
                                           coefficient=2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, 2.0*simulation.forces[0].values,
        label='$C_d$ ($\Delta t= 2 \cdot 10^{-4}$)',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(loose.forces[0].times, 2.0*loose.forces[0].values,
        label='$C_d$ ($\Delta t= 4 \cdot 10^{-4}$)',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ ($\Delta t= 2 \cdot 10^{-4}$)',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(loose.forces[1].times, 2.0*loose.forces[1].values,
        label='$C_l$ ($\Delta t= 4 \cdot 10^{-4}$)',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([0.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 13})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsCompareDt.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
