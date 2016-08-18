"""
Generates Figure 9 of the manuscript 
as a .pdf file named `petibm011_forceCoefficientsRe2000AoA35.pdf`.
"""

import os
import shutil
import yaml
import argparse
import warnings

from matplotlib import pyplot

import snake
from snake.petibm.simulation import PetIBMSimulation
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


# Computes the mean force coefficients from the PetIBM simulation
# that uses shifted markers (rotation around the center of mass).
# The force coefficients are averaged between 32 and 64 time-units.
simulation_directory = dirs['petibm011_forceCoefficientsRe2000AoA35']['displaced']
simulation = PetIBMSimulation(description='PetIBM (displaced markers)',
                              directory=simulation_directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

# Computes the mean force coefficients from the PetIBM simulation
# that uses exact markers (rotation around the origin (0,0)).
# The set of markers is identical to the one used in Krishnan et al. (2014).
# The force coefficients are averaged between 32 and 64 time-units.
simulation_directory = dirs['petibm011_forceCoefficientsRe2000AoA35']['original']
simulation2 = PetIBMSimulation(description='PetIBM (original markers)',
                               directory=simulation_directory)
simulation2.read_forces()
simulation2.get_mean_forces(limits=[32.0, 64.0])
simulation2.get_strouhal(limits=[32.0, 64.0], order=200)

# Computes the mean force coefficients from the cuIBM simulation 
# reported in Krishnan et al. (2014).
# The force coefficients are averaged between 32 and 64 time-units.
krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path=os.path.join(os.environ['SNAKE'],
                                            'resources',
                                            'flyingSnake2d_cuibm_anush',
                                            'flyingSnake2dRe2000AoA35',
                                            'forces'))
krishnan.get_mean_forces(limits=[32.0, 64.0])
krishnan.get_strouhal(limits=[32.0, 64.0], order=200)

# Creates a table with the time-averaged force coefficients
# and the mean Strouhal number.
dataframe = krishnan.create_dataframe_forces(display_strouhal=True,
                                             display_coefficients=True,
                                             coefficient=2.0)
dataframe2 = simulation.create_dataframe_forces(display_strouhal=True,
                                                display_coefficients=True,
                                                coefficient=2.0)
dataframe3 = simulation2.create_dataframe_forces(display_strouhal=True,
                                                display_coefficients=True,
                                                coefficient=2.0)
dataframe = dataframe.append([dataframe2, dataframe3])
print(dataframe)

# Plots the instantaneous force coefficients and compares to those reported
# in Krishnan et al. (2014).
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
file_path_in_1 = os.path.join(args.save_directory,
                    'petibm011_forceCoefficientsRe2000AoA35CompareKrishnan.pdf')
pyplot.savefig(file_path_in_1,
               bbox_inches='tight',
               format='pdf',
               dpi=300)
pyplot.savefig(file_path_in_1.replace('.pdf', '.png'),
               bbox_inches='tight',
               format='png',
               dpi=300)

# Plots the instantaneous force coefficients from the simulation using shifted
# markers and from the simulation using exact markers.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation2.forces[0].times, 2.0*simulation2.forces[0].values,
        label='$C_d$ - original markers',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(simulation.forces[0].times, 2.0*simulation.forces[0].values,
        label='$C_d$ - displaced markers',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(simulation2.forces[1].times, 2.0*simulation2.forces[1].values,
        label='$C_l$ - original markers',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(simulation.forces[1].times, 2.0*simulation.forces[1].values,
        label='$C_l$ - displaced markers',
        color='#111111',
        linestyle=':',
        linewidth=2,
        zorder=11)
ax.axis([20.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
file_path_in_2 = os.path.join(args.save_directory,
                     'petibm011_forceCoefficientsRe2000AoA35CompareMarkers.pdf')
pyplot.savefig(file_path_in_2,
               bbox_inches='tight',
               format='pdf',
               dpi=300)
pyplot.savefig(file_path_in_2.replace('.pdf', '.png'),
               bbox_inches='tight',
               format='png',
               dpi=300)

# Merges two .pdf files into one for the manuscript and remove the two .pdf files.
file_path_out = os.path.join(args.save_directory,
                             'petibm011_forceCoefficientsRe2000AoA35.pdf')
os.system('pdfjam {} {} --nup 1x2 --outfile {}'.format(file_path_in_1,
                                                       file_path_in_2,
                                                       file_path_out))
os.remove(file_path_in_1)
os.remove(file_path_in_2)
