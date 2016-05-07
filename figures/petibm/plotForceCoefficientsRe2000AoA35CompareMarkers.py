# file: plotForceCoefficientsRe2000AoA35CompareMarkers.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the instantaneous force coefficients
#              and compare to simulation with displaced markers.
# Run this script from the simulation directory.


import os

from matplotlib import pyplot

from snake.petibm.simulation import PetIBMSimulation


simulation = PetIBMSimulation(description='original markers',
                              directory=os.path.join(os.environ['HOME'],
                                                     'simulations_PetIBM',
                                                     'flyingSnake',
                                                     '2d',
                                                     'cuibmGrid',
                                                     'velocityBiCGStabPoissonBiCGStab',
                                                     'flyingSnake2dRe2000AoA35_20160426'))
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

other = PetIBMSimulation(description='displaced markers',
                         directory=os.path.join(os.environ['HOME'],
                                                'simulations_PetIBM',
                                                'flyingSnake',
                                                '2d',
                                                'cuibmGrid',
                                                'velocityCGPoissonBiCGStab',
                                                'flyingSnake2dRe2000AoA35_bugFixPoisson_20160202'))
other.read_forces()
other.get_mean_forces(limits=[32.0, 64.0])
other.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = simulation.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = other.create_dataframe_forces(display_strouhal=True,
                                           display_coefficients=True,
                                           coefficient=2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

pyplot.style.use(os.path.join(os.environ['SNAKE'],
                              'snake',
                              'styles',
                              'snakeReproducibility.mplstyle'))
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, 2.0*simulation.forces[0].values,
        label='$C_d$ - original markers',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(other.forces[0].times, 2.0*other.forces[0].values,
        label='$C_d$ - displaced markers',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ - original markers',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(other.forces[1].times, 2.0*other.forces[1].values,
        label='$C_l$ - displaced markers',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([20.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
pyplot.savefig('petibm-0.1.1_forceCoefficientsRe2000AoA35CompareMarkers.pdf',
               bbox_inches='tight',
               format='pdf')