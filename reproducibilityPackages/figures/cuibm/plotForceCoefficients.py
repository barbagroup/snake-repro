"""
Generates Figure 11 of the manuscript 
as a .pdf file named `cuibm_forceCoefficients.pdf`.
"""

import os
import yaml
import argparse
import warnings

from matplotlib import pyplot

import snake
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


# Plots the instantaneous force coefficients at Re=1000 and AoA=35deg
# using a current version of cuIBM with CUSP-0.5.1
# and compares to the results reported in Krishnan et al. (2014).
simulation_directory = dirs['cuibm-current-cusp051']['Re1000AoA35']
simulation = CuIBMSimulation(description='cuIBM (current) - cusp-0.5.1',
                             directory=simulation_directory)
simulation.read_forces()
simulation.get_mean_forces(limits=[32.0, 64.0])
simulation.get_strouhal(limits=[32.0, 64.0], order=200)

krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path=os.path.join(os.environ['SNAKE'],
                                            'resources',
                                            'flyingSnake2d_cuibm_anush',
                                            'flyingSnake2dRe1000AoA35',
                                            'forces'))
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
        label='$C_d$ - current - CUSP-0.5.1',
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
        label='$C_l$ - current - CUSP-0.5.1',
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
ax.axis([40.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
file_path_in_1 = os.path.join(args.save_directory, 
                      'cuibm-current-cusp051_forceCoefficientsRe1000AoA35.png')
pyplot.savefig(file_path_in_1,
               bbox_inches='tight',
               format='png',
               dpi=300)


# Plots the instantaneous force coefficients at Re=2000 and AoA=30deg
# using a current version of cuIBM with CUSP-0.5.1
# and compares to the results reported in Krishnan et al. (2014).
simulation_directory = dirs['cuibm-current-cusp051']['Re2000AoA30']
simulation = CuIBMSimulation(description='cuIBM (current) - cusp-0.5.1',
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
                                               coefficient=2.0)
dataframe2 = krishnan.create_dataframe_forces(display_strouhal=True,
                                              display_coefficients=True,
                                              coefficient=2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(simulation.forces[0].times, 2.0*simulation.forces[0].values,
        label='$C_d$ - current - CUSP-0.5.1',
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
        label='$C_l$ - current - CUSP-0.5.1',
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
ax.axis([40.0, 80.0, 0.5, 3.0])
ax.legend(ncol=2, loc='upper right')
file_path_in_2 = os.path.join(args.save_directory, 
                      'cuibm-current-cusp051_forceCoefficientsRe2000AoA30.png')
pyplot.savefig(file_path_in_2,
               bbox_inches='tight',
               format='png',
               dpi=300)


# Plots the instantaneous force coefficients at Re=2000 and AoA=35deg
# using a version of cuIBM closed to what Krishnan et al. (2014) used
# and using CUSP-0.4.0
simulation_directory = dirs['cuibm-revision86-cusp040']['Re2000AoA35']
revision86 = CuIBMSimulation(description='cuIBM (revision86) - cusp-0.4.0',
                             directory=simulation_directory)
revision86.read_forces()
revision86.get_mean_forces(limits=[32.0, 64.0])
revision86.get_strouhal(limits=[32.0, 64.0], order=200)

krishnan = CuIBMSimulation(description='Krishnan et al. (2014)')
krishnan.read_forces(file_path=os.path.join(os.environ['SNAKE'],
                                            'resources',
                                            'flyingSnake2d_cuibm_anush',
                                            'flyingSnake2dRe2000AoA35',
                                            'forces'))
krishnan.get_mean_forces(limits=[32.0, 64.0])
krishnan.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = revision86.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = krishnan.create_dataframe_forces(display_strouhal=True,
                                              display_coefficients=True,
                                              coefficient=2.0)
dataframe = dataframe.append(dataframe2)
print(dataframe)

fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(revision86.forces[0].times, 2.0*revision86.forces[0].values,
        label='$C_d$ - revision86 - CUSP-0.4.0',
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
ax.plot(revision86.forces[1].times, 2.0*revision86.forces[1].values,
        label='$C_l$ - revision86 - CUSP-0.4.0',
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
ax.axis([40.0, 80.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right')
file_path_in_3 = os.path.join(args.save_directory, 
                            'cuibm-revision86_forceCoefficientsRe2000AoA35.png')
pyplot.savefig(file_path_in_3,
               bbox_inches='tight',
               format='png',
               dpi=300)


# Plots the instantaneous force coefficients at Re=2000 and AoA=35 deg
# from three simulations: old version of cuIBM using CUSP-0.4.0, current version
# using CUSP-0.4.0, and current version using CUSP-0.5.1.
simulation_directory = dirs['cuibm-current-cusp040']['Re2000AoA35']
current040 = CuIBMSimulation(description='cuIBM (current) - CUSP-0.4.0',
                             directory=simulation_directory)
current040.read_forces()
current040.get_mean_forces(limits=[32.0, 64.0])
current040.get_strouhal(limits=[32.0, 64.0], order=200)

simulation_directory = dirs['cuibm-current-cusp051']['Re2000AoA35']
current051 = CuIBMSimulation(description='cuIBM (current) - CUSP-0.5.1',
                             directory=simulation_directory)
current051.read_forces()
current051.get_mean_forces(limits=[32.0, 64.0])
current051.get_strouhal(limits=[32.0, 64.0], order=200)

dataframe = revision86.create_dataframe_forces(display_strouhal=True,
                                               display_coefficients=True,
                                               coefficient=2.0)
dataframe2 = current040.create_dataframe_forces(display_strouhal=True,
                                                display_coefficients=True,
                                                coefficient=2.0)
dataframe3 = current051.create_dataframe_forces(display_strouhal=True,
                                                display_coefficients=True,
                                                coefficient=2.0)
dataframe = dataframe.append([dataframe2, dataframe3])
print(dataframe)

fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
ax.plot(current040.forces[0].times, 2.0*current040.forces[0].values,
        label='$C_d$ - current - CUSP-0.4.0',
        color='#377eb8',
        linestyle='-',
        linewidth=2,
        zorder=10)
ax.plot(current051.forces[0].times, 2.0*current051.forces[0].values,
        label='$C_d$ - current - CUSP-0.5.1',
        color='green',
        linestyle='-',
        linewidth=1,
        zorder=11)
ax.plot(revision86.forces[0].times, 2.0*revision86.forces[0].values,
        label='$C_d$ - old - CUSP-0.4.0',
        color='#111111',
        linestyle='-',
        linewidth=1,
        zorder=12)
ax.plot(current040.forces[1].times, 2.0*current040.forces[1].values,
        label='$C_l$ - current - CUSP-0.4.0',
        color='#ff7f00',
        linewidth=2,
        linestyle='-',
        zorder=10)
ax.plot(current051.forces[1].times, 2.0*current051.forces[1].values,
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
file_path_in_4 = os.path.join(args.save_directory,
                    'cuibm-current-revision86_forceCoefficientsRe2000AoA35.png')
pyplot.savefig(file_path_in_4,
               bbox_inches='tight',
               format='png',
               dpi=300)

# convert two .png into a single one (side by side)
os.system('convert +append {} {} top.png'.format(file_path_in_1,
                                                 file_path_in_2))
os.system('convert +append {} {} bottom.png'.format(file_path_in_3,
                                                    file_path_in_4))
# concatenate the two new .png files into one .png (one after one)
file_path_out = os.path.join(args.save_directory,
                             'cuibm_forceCoefficients.png')
os.system('convert -append top.png bottom.png {}'.format(file_path_out))
# concatenate the two new .png files into one .pdf
os.system('convert -append top.png bottom.png {}'.format(file_path_out.replace('.png', '.pdf')))

# remove temporary files
os.remove(file_path_in_1)
os.remove(file_path_in_2)
os.remove(file_path_in_3)
os.remove(file_path_in_4)
os.remove('top.png')
os.remove('bottom.png')
