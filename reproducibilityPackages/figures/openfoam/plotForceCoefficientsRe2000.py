"""
Generates Figure 4 of the manuscript 
as a .pdf file named `openfoam_forceCoefficientsRe2000.pdf`.
"""

import os
import yaml
import shutil
import argparse
import warnings

from matplotlib import pyplot

import snake
from snake.openfoam.simulation import OpenFOAMSimulation
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
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

# Plots the force coefficients at Re=2000 and AoA=30deg
# and compares to the results reported in Krishnan et al. (2014).
simulation_directory = dirs['openfoam_forceCoefficientsRe2000']['Re2000AoA30']
simulation = OpenFOAMSimulation(description='IcoFOAM',
                                directory=simulation_directory)
simulation.read_forces(display_coefficients=True)
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
                                               display_coefficients=True)
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
ax.plot(simulation.forces[0].times, simulation.forces[0].values,
        label='$C_d$ - IcoFOAM',
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
ax.plot(simulation.forces[1].times, simulation.forces[1].values,
        label='$C_l$ - IcoFOAM',
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
                              'openfoam_forceCoefficientsRe2000AoA30.png')
pyplot.savefig(file_path_in_1,
               bbox_inches='tight',
               format='png',
               dpi=300)


# Plots the force coefficients at Re=2000 and AoA=35deg
# and compares to the results reported in Krishnan et al. (2014).
simulation_directory = dirs['openfoam_forceCoefficientsRe2000']['Re2000AoA35']
simulation = OpenFOAMSimulation(description='IcoFOAM',
                                directory=simulation_directory)
simulation.read_forces(display_coefficients=True)
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
                                               display_coefficients=True)
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
ax.plot(simulation.forces[0].times, simulation.forces[0].values,
        label='$C_d$ - IcoFOAM',
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
ax.plot(simulation.forces[1].times, simulation.forces[1].values,
        label='$C_l$ - IcoFOAM',
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
                              'openfoam_forceCoefficientsRe2000AoA35.png')
pyplot.savefig(file_path_in_2,
               bbox_inches='tight',
               format='png',
               dpi=300)

# concatenate the two .png files into one
file_path_out = os.path.join(args.save_directory,
                             'openfoam_forceCoefficientsRe2000.png')
os.system('convert -append {} {} {}'.format(file_path_in_1,
                                            file_path_in_2,
                                            file_path_out))
# convert the .png file into a .pdf
os.system('convert -append {} {} {}'.format(file_path_in_1,
                                            file_path_in_2,
                                            file_path_out.replace('.png', '.pdf')))
# remove the two initial .png files
os.remove(file_path_in_1)
os.remove(file_path_in_2)
