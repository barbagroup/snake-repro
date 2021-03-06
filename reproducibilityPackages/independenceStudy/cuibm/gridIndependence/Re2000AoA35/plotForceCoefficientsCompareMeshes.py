"""
Plots the instantaneous force coefficients obtained on a grid with spacing 
h=0.006 in the uniform region and compares with the solution obtained on a finer
mesh (h=0.004).
"""

import os
import warnings

from matplotlib import pyplot

import snake
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))

# Computes the mean force coefficients from the cuIBM simulation
# with grid-spacing h=0.004 in the uniform region.
# The force coefficients are averaged between 32 and 64 time-units.
simulation_directory = os.path.join(os.path.dirname(__file__), 
                                    'h0.004')
simulation = CuIBMSimulation(description='h=0.004',
                             directory=simulation_directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])

# Computes the mean force coefficients from the cuIBM simulation
# with grid-spacing h=0.006 in the uniform region.
# The force coefficients are averaged between 32 and 64 time-units.
simulation_directory = os.path.join(os.path.dirname(__file__), 
                                    'h0.006_vatol16_patol8_dt0.0002')
simulation2 = CuIBMSimulation(description='h=0.006',
                              directory=simulation_directory)
simulation2.read_forces()
simulation2.get_mean_forces(limits=[32.0, 64.0])

# Creates a table with the time-averaged force coefficients.
dataframe = simulation.create_dataframe_forces(display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = simulation2.create_dataframe_forces(display_coefficients=True,
                                                 coefficient=2.0)
dataframe = dataframe.append([dataframe2])
print(dataframe)

# Plots the instantaneous force coefficients from the simulation using shifted
# markers and from the simulation using exact markers.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation2.forces[0].times, 2.0*simulation2.forces[0].values,
        label='$C_d$ - $h=0.006$',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(simulation.forces[0].times, 2.0*simulation.forces[0].values,
        label='$C_d$ - $h=0.004$',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation2.forces[1].times, 2.0*simulation2.forces[1].values,
        label='$C_l$ - $h=0.006$',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ - $h=0.004$',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([0.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsCompareMeshes.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
