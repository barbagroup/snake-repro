"""
Plots and compares the instantaneous force coefficients obtained by computing
the numerical solution on two AMR discretizations: one where the smallest
grid-spacing is h=0.004, the other is h=0.002.
All other parameters remain unchanged.
The force coefficients are also averaged between 32 and 64 time-units.

The script generates the figure `forceCoefficientsCompareMeshes.png`
saved in the present directory.
"""

import os

from matplotlib import pyplot

import snake
from snake.ibamr.simulation import IBAMRSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


directory = os.path.join(os.path.dirname(__file__),
                         'h0.002')
simulation = IBAMRSimulation(description='h=0.002',
                             directory=directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])


directory = os.path.join(os.path.dirname(__file__),
                         'h0.004')
other = IBAMRSimulation(description='h=0.004',
                        directory=directory)
other.read_forces()
other.get_mean_forces(limits=[32.0, 64.0])

dataframe = simulation.create_dataframe_forces(display_coefficients=True,
                                               coefficient=-2.0)
dataframe2 = other.create_dataframe_forces(display_coefficients=True,
                                           coefficient=-2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

# Plots the instantaneous force coefficients.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, -2.0*simulation.forces[0].values,
        label='$C_d$ (fine - $h=0.002$)',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(other.forces[0].times, -2.0*other.forces[0].values,
        label='$C_d$ (coarse - $h=0.004$)',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, -2.0*simulation.forces[1].values,
        label='$C_l$ (fine - $h=0.002$)',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(other.forces[1].times, -2.0*other.forces[1].values,
        label='$C_l$ (coarse - $h=0.004$)',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([0.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 10})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsCompareMeshes.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
