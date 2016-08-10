"""
Generates Figure 3 of the manuscript 
as a .pdf file named `openfoam_forceCoefficientsVsAoA.pdf`.
"""

import os
import yaml
import shutil
import argparse

from matplotlib import pyplot

import snake
from snake.openfoam.simulation import OpenFOAMSimulation
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


# Computes the mean coefficients from the OpenFOAM simulations.
# The force coefficients are averaged between 32 and 64 time-units.
cd_openfoam, cl_openfoam = [], []
for re in ['Re1000', 'Re2000']:
  for aoa in ['AoA25', 'AoA30', 'AoA35', 'AoA40']:
    simulation_directory = dirs['openfoam_forceCoefficientsVsAoA'][re][aoa]
    simulation = OpenFOAMSimulation(directory=simulation_directory)
    simulation.read_forces(display_coefficients=True)
    simulation.get_mean_forces(limits=[32.0, 64.0])
    cd_openfoam.append(simulation.forces[0].mean['value'])
    cl_openfoam.append(simulation.forces[1].mean['value'])

# Computes the mean coefficients from the cuIBM simulations
# reported in Krishnan et al. (2014).
# The force coefficients are averaged between 32 and 64 time-units.
cd_krishnan, cl_krishnan = [], []
for re in ['Re1000', 'Re2000']:
  for aoa in ['AoA25', 'AoA30', 'AoA35', 'AoA40']:
    simulation_directory = os.path.join(os.environ['SNAKE'],
                                        'resources',
                                        'flyingSnake2d_cuibm_anush',
                                        'flyingSnake2d'+re+aoa)
    krishnan = CuIBMSimulation(directory=simulation_directory)
    krishnan.read_forces()
    krishnan.get_mean_forces(limits=[32.0, 64.0])
    cd_krishnan.append(2.0*krishnan.forces[0].mean['value'])
    cl_krishnan.append(2.0*krishnan.forces[1].mean['value'])


# plot figure
aoa  = [25, 30, 35, 40]
pyplot.style.use(os.path.join(os.environ['SNAKE'], 
                              'snake', 
                              'styles', 
                              'snakeReproducibility.mplstyle'))
fig = pyplot.figure(figsize=(6, 8))
gs = gridspec.GridSpec(3, 2, 
                       height_ratios=[1, 1, 0.5])
ax1 = pyplot.subplot(gs[0, :])
ax2 = pyplot.subplot(gs[1, :])
ax3 = pyplot.subplot(gs[2, 0])
ax4 = pyplot.subplot(gs[2, 1])
gs.update(wspace=0.5, hspace=0.1)
# drag coefficient versus angle-of-attack
ax1.grid(True, zorder=0)
ax1.set_ylabel('drag coefficient')
# Re=1000
ax1.plot(aoa, cd_openfoam[:len(aoa)],  
         label='IcoFOAM',
         color='#1B9E77', 
         linestyle='-', 
         marker='o', 
         zorder=11)
ax1.plot(aoa, cd_krishnan[:len(aoa)],  
         label='Krishnan et al. (2014)',
         color='#666666', 
         linestyle=':', 
         marker='o',
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
# Re=2000
ax1.plot(aoa, cd_openfoam[len(aoa):],  
         label='IcoFOAM',
         color='#D95F02', 
         linestyle='-', 
         marker='s', 
         zorder=11)
ax1.plot(aoa, cd_krishnan[len(aoa):],  
         label='Krishnan et al. (2014)',
         color='#666666', 
         linestyle='--', 
         marker='s',
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
ax1.set_xlim(aoa[0]-1.0, aoa[-1]+1.0)
ax1.set_xticks(aoa)
ax1.set_xticklabels([])
# lift coefficient versus angle-of-attack
ax2.grid(True, zorder=0)
ax2.set_xlabel('angle of attack')
ax2.set_ylabel('lift coefficient')
# Re=1000
ax2.plot(aoa, cl_openfoam[:len(aoa)],  
         label='IcoFOAM',
         color='#1B9E77', 
         linestyle='-', 
         marker='o',
         zorder=11)
ax2.plot(aoa, cl_krishnan[:len(aoa)],  
         label='Krishnan et al. (2014)',
         color='#666666', 
         linestyle=':',
         marker='o', 
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
# Re=2000
ax2.plot(aoa, cl_openfoam[len(aoa):],  
         label='IcoFOAM',
         color='#D95F02',
         linestyle='-', 
         marker='s',
         zorder=11)
ax2.plot(aoa, cl_krishnan[len(aoa):],  
         label='Krishnan et al. (2014)',
         color='#666666', linestyle='--', 
         marker='s',
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
ax2.set_xlim(aoa[0]-1.0, aoa[-1]+1.0)
aoa_labels = [str(a)+'$^o$' for a in aoa]
ax2.set_xticks(aoa)
ax2.set_xticklabels(aoa_labels)
# create legend
handles, labels = ax1.get_legend_handles_labels()
ax3.axis('off')
legend = ax3.legend(handles[:2], 
                    labels[:2], 
                    title='Re = 1000',
                    loc='lower left',
                    prop={'size': 9},
                    scatterpoints=1)
legend.get_title().set_fontsize('9')
ax4.axis('off')
legend = ax4.legend(handles[2:], 
                    labels[2:], 
                    title='Re = 2000',
                    loc='lower right',
                    prop={'size': 9},
                    scatterpoints=1)
legend.get_title().set_fontsize('9')
# save figure in .png and .pdf formats
file_path_out = os.path.join(args.save_directory, 
                             'openfoam_forceCoefficientsVsAoA.pdf')
pyplot.savefig(file_path_out,
               bbox_inches='tight',
               format='pdf',
               dpi=300)
pyplot.savefig(file_path_out.replace('.pdf', '.png'),
               bbox_inches='tight',
               format='png',
               dpi=300)
