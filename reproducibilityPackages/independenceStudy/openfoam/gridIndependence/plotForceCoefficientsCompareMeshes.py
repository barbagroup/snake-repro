"""
Plots the instantaneous force coefficients from the simulation on two different 
meshes.
The first mesh (reported in our manuscript) has a minimum grid-spacing of 
h=0.004 in the vicinity of the bluff-body (about 3.4 million cells).
The second mesh has even smaller cells in the vicinity of the body (h=0.002) 
and contains about 5.3 million cells.

The script generates the figure `forceCoefficientsCompareMeshes.png` saved 
in the present directory.
"""

import os
import warnings

from matplotlib import pyplot

import snake
from snake.openfoam.simulation import OpenFOAMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


# Reads the instantaneous forces from the simulation on the fine grid.
# The force coefficients are averaged between 32 and 64 time-units.
directory = os.path.join(os.path.dirname(__file__),
                         'h0.002')
simulation = OpenFOAMSimulation(description='fine (5.3M cells)',
                                directory=directory)
simulation.read_forces(display_coefficients=True)
simulation.get_mean_forces(limits=[32.0, 64.0])

# Reads the instantaneous forces from the simulation on the coarse grid.
# The force coefficients are averaged between 32 and 64 time-units.
directory = os.path.join(os.path.dirname(__file__),
                         'h0.004')
other = OpenFOAMSimulation(description='coarse (3.4M cells)',
                           directory=directory)
other.read_forces(display_coefficients=True)
other.get_mean_forces(limits=[32.0, 64.0])

# Displays the time-averaged force coefficients into a table.
dataframe = simulation.create_dataframe_forces(display_coefficients=True)
dataframe2 = other.create_dataframe_forces(display_coefficients=True)
dataframe = dataframe.append(dataframe2)
print(dataframe)

# Plots the instantaneous force coefficients
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, simulation.forces[0].values,
        label='$C_d$ (fine - 5.3M cells)',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(other.forces[0].times, other.forces[0].values,
        label='$C_d$ (coarse - 3.4M cells)',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, simulation.forces[1].values,
        label='$C_l$ (fine - 5.3M cells)',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(other.forces[1].times, other.forces[1].values,
        label='$C_l$ (coarse - 3.4M cells)',
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
