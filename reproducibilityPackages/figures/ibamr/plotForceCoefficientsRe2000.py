"""
Generates Figure 7 of the paper 
as a .pdf file named `ibamr_forceCoefficientsRe2000.pdf`.
"""

import os
import yaml
import argparse

from matplotlib import pyplot

import snake
from snake.ibamr.simulation import IBAMRSimulation
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.1':
  warnings.warn('The figures were originally created with snake-0.1.1, '+
                'you are using snake-{}'.format(snake.__version__))


# initialization
script_directory = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument('--map', 
                    dest='map', 
                    type=str, 
                    default=os.path.join(script_directory, 'map.yaml'), 
                    help='file containing the list of simulation directories')
parser.add_argument('--save-dir', 
                    dest='save_directory', 
                    type=str, 
                    default=script_directory, 
                    help='directory where to save the figures')
args = parser.parse_args()
with open(args.map, 'r') as infile:
  dirs = yaml.load(infile)


# plot the instantaneous force coefficients at Re=2000 and AoA=30deg
# and compare to the results reported in Kirshnan et al. (2014)
simulation_directory = dirs['ibamr_forceCoefficientsRe2000']['AoA30']
simulation = IBAMRSimulation(description='IBAMR',
                             directory=simulation_directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path=os.path.join(os.environ['SNAKE'],
                                            'resources',
                                            'flyingSnake2d_cuibm_anush',
                                            'flyingSnake2dRe2000AoA30',
                                            'forces'))
krishnan.get_mean_forces(limits=[32.0, 64.0])
krishnan.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = simulation.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=-2.0)
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
ax.plot(simulation.forces[0].times, -2.0*simulation.forces[0].values,
        label='$C_d$ - IBAMR',
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
ax.plot(simulation.forces[1].times, -2.0*simulation.forces[1].values,
        label='$C_l$ - IBAMR',
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
ax.axis([20.0, 80.0, 0.5, 3.0])
ax.legend(ncol=2, loc='upper right')
file_path_in_1 = os.path.join(args.save_directory, 
                              'ibamr_forceCoefficientsRe2000AoA30.pdf')
pyplot.savefig(file_path_in_1,
               bbox_inches='tight',
               format='pdf',
               dpi=300)
pyplot.savefig(file_path_in_1.replace('.pdf', '.png'),
               bbox_inches='tight',
               format='png',
               dpi=300)


# plot the instantaneous force coefficients at Re=2000 and AoA=35deg
# and compare to the results reported in Kirshnan et al. (2014)
simulation_directory = dirs['ibamr_forceCoefficientsRe2000']['AoA35']
simulation = IBAMRSimulation(description='IBAMR',
                             directory=simulation_directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path=os.path.join(os.environ['SNAKE'],
                                            'resources',
                                            'flyingSnake2d_cuibm_anush',
                                            'flyingSnake2dRe2000AoA35',
                                            'forces'))
krishnan.get_mean_forces(limits=[32.0, 64.0])
krishnan.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = simulation.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=-2.0)
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
ax.plot(simulation.forces[0].times, -2.0*simulation.forces[0].values,
        label='$C_d$ - IBAMR',
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
ax.plot(simulation.forces[1].times, -2.0*simulation.forces[1].values,
        label='$C_l$ - IBAMR',
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
ax.axis([20.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
file_path_in_2 = os.path.join(args.save_directory, 
                              'ibamr_forceCoefficientsRe2000AoA35.pdf')
pyplot.savefig(file_path_in_2,
               bbox_inches='tight',
               format='pdf',
               dpi=300)
pyplot.savefig(file_path_in_2.replace('.pdf', '.png'),
               bbox_inches='tight',
               format='png',
               dpi=300)


# merge two .pdf files into one in a 1x2 formation
file_path_out = os.path.join(args.save_directory, 
                             'ibamr_forceCoefficientsRe2000.pdf')
os.system('pdfjam {} {} --nup 1x2 --outfile {}'
          .format(file_path_in_1, file_path_in_2, file_path_out))
os.remove(file_path_in_1)
os.remove(file_path_in_2)
