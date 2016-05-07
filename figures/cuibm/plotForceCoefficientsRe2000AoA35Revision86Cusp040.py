# file: plotForceCoefficientsRe2000AoA35Revision86Cusp040.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the instantaneous force coefficients
#              and compare to results from Krishnan et al. (2014).
# Run this script from the simulation directory.


import os

from matplotlib import pyplot

from snake.cuibm.simulation import CuIBMSimulation


simulation = CuIBMSimulation(description='cuIBM (old version) - cusp-0.4.0',
                             directory=os.path.join(os.environ['HOME'],
                                                    'simulations_cuIBM',
                                                    'revision86-cusp-0.4.0',
                                                    'flyingSnake2dRe2000AoA35_20160502',
                                                    'numericalSolution'))
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
        label='$C_d$ - cuIBM (old version) - cusp-0.4.0',
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
        label='$C_l$ - cuIBM (old version) - cusp-0.4.0',
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
ax.axis([40.0, 80.0, 0.75, 4.0])
ax.legend(ncol=1, loc='upper right')
pyplot.savefig('cuibm-revision86-cusp-0.4.0_forceCoefficientsRe2000AoA35.pdf',
               bbox_inches='tight',
               format='pdf')