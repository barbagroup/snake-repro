# file: plotForceCoefficientsRe2000AoA35.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the instantaneous force coefficients
#              and compares to results from Krishnan et al. (2014).


import os

from matplotlib import pyplot

from snake.petibm.simulation import PetIBMSimulation
from snake.cuibm.simulation import CuIBMSimulation


simulation = PetIBMSimulation(description='PetIBM',
                              directory=os.path.join(os.environ['HOME'],
                                                     'simulations_PetIBM',
                                                     'flyingSnake',
                                                     '2d',
                                                     'cuibmGrid',
                                                     'velocityCGPoissonBiCGStab',
                                                     'flyingSnake2dRe2000AoA35_bugFixPoisson_20160202'))
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path='{}/resources/flyingSnake2d_cuibm_anush/'
                               'flyingSnake2dRe2000AoA35/forces'
                               ''.format(os.environ['SNAKE']))
krishnan.get_mean_forces(limits=[32.0, 64.0])
krishnan.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = simulation.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = krishnan.create_dataframe_forces(display_strouhal=True,
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
        label='$C_d$ - PetIBM',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(krishnan.forces[0].times, 2.0*krishnan.forces[0].values,
        label='$C_d$ - Krishnan et al. (2014)',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ - PetIBM',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(krishnan.forces[1].times, 2.0*krishnan.forces[1].values,
        label='$C_l$ - Krishnan et al. (2014)',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([0.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
pyplot.savefig('petibm-0.1.1_forceCoefficientsRe2000AoA35.pdf',
               bbox_inches='tight',
               format='pdf')
