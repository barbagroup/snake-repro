"""
Generates Figure 1 of the manuscript 
as a .pdf file named `openfoam_vorticity52Re2000AoA35_gmshZeroGradient.pdf`.
"""

import os
import yaml
import shutil
import argparse

from matplotlib import pyplot

import snake
from snake.openfoam.simulation import OpenFOAMSimulation


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

simulation_directory = dirs['openfoam_vorticity52Re2000AoA35_gmshZeroGradient']['Re2000AoA35']
simulation = OpenFOAMSimulation(directory=simulation_directory)
simulation.plot_field_contours_paraview('vorticity',
                                        field_range=(-5.0, 5.0),
                                        view=(-5.0, -8.0, 10.0, 2.0),
                                        times=(52.0, 52.0, 1.0),
                                        width=1000,
                                        colormap='RdBu_r')

# copy the .png file
file_path_source = os.path.join(simulation.directory,
                                'images',
                                'vorticity_-5.00_-8.00_10.00_2.00',
                                'vorticity052.00.png')
file_path_detination = os.path.join(args.save_directory,
                        'openfoam_vorticity52Re2000AoA35_gmshZeroGradient.png')
shutil.copy(file_path_source, file_path_detination)
# convert into .pdf file
os.system('convert {} {}'.format(file_path_detination,
                                 file_path_detination.replace('.png', '.pdf')))
