# file: plotForceCoefficientsRe2000AoA35CurrentRevision86.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the instantaneous force coefficients
#              and compare with results from revision 86 and current version 
#              with cusp-0.5.1.
# Run this script from the simulation directory.


import os

from matplotlib import pyplot

from snake.cuibm.simulation import CuIBMSimulation


simulation = CuIBMSimulation(description='cuIBM (current) - CUSP-0.4.0',
                             directory=os.path.join(os.environ['HOME'],
                                                    'simulations_cuIBM',
                                                    'production-cusp-0.4.0',
                                                    'flyingSnake2dRe2000AoA35_20160502'))
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

other = CuIBMSimulation(description='cuIBM (current) - CUSP-0.5.1',
                        directory=os.path.join(os.environ['HOME'],
                                               'simulations_cuIBM',
                                               'production-cusp-0.5.1',
                                               'flyingSnake2dRe2000AoA35_20160502'))
other.read_forces()
other.get_mean_forces(limits=[32.0, 64.0])
other.get_strouhal(limits=[32.0, 64.0], order=200)

revision86 = CuIBMSimulation(description='cuIBM (old) - CUSP-0.4.0',
                             directory=os.path.join(os.environ['HOME'],
                                                    'simulations_cuIBM',
                                                    'revision86-cusp-0.4.0',
                                                    'flyingSnake2dRe2000AoA35_20160502',
                                                    'numericalSolution'))
revision86.read_forces()
revision86.get_mean_forces(limits=[32.0, 64.0])
revision86.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = simulation.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = other.create_dataframe_forces(display_strouhal=True,
                                           display_coefficients=True,
                                           coefficient=2.0)
dataframe3 = revision86.create_dataframe_forces(display_strouhal=True,
                                                display_coefficients=True,
                                                coefficient=2.0)
dataframe = dataframe.append(dataframe2)
dataframe = dataframe.append(dataframe3)
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
        label='$C_d$ - current - CUSP-0.4.0',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(other.forces[0].times, 2.0*other.forces[0].values,
        label='$C_d$ - current - CUSP-0.5.1',
        color='green',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(revision86.forces[0].times, 2.0*revision86.forces[0].values,
        label='$C_d$ - old - CUSP-0.5.1',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=12)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ - current - CUSP-0.4.0',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(other.forces[1].times, 2.0*other.forces[1].values,
        label='$C_l$ - current - CUSP-0.5.1',
        color='red',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(revision86.forces[1].times, 2.0*revision86.forces[1].values,
        label='$C_l$ - old - CUSP-0.4.0',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=12)
ax.axis([50.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
pyplot.savefig('cuibm-current-revision86_forceCoefficientsRe2000AoA35.pdf',
               bbox_inches='tight',
               format='pdf')