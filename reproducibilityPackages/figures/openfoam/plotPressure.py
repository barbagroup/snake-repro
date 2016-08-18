"""
Generates Figure 2 of the manuscript 
as a .pdf file named `openfoam_pressureRe2000AoA35_gmshZeroGradient.pdf`.
"""

import os
import yaml
import shutil
import argparse
import warnings

from matplotlib import pyplot

import snake
from snake.openfoam.simulation import OpenFOAMSimulation


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

simulation_directory = dirs['openfoam_pressureRe2000AoA35_gmshZeroGradient']['Re2000AoA35']
simulation = OpenFOAMSimulation(directory=simulation_directory)
simulation.plot_field_contours_paraview('pressure',
                                        field_range=(-1.0, 0.5),
                                        view=(-2.0, -3.0, 15.0, 3.0),
                                        times=(52.0, 53.0, 1.0),
                                        width=1000,
                                        colormap='viridis')

# concatenate the two .png files
file_path_source_1 = os.path.join(simulation.directory,
                                  'images',
                                  'pressure_-2.00_-3.00_15.00_3.00',
                                  'pressure052.00.png')
file_path_source_2 = os.path.join(simulation.directory,
                                  'images',
                                  'pressure_-2.00_-3.00_15.00_3.00',
                                  'pressure053.00.png')
file_path_destination = os.path.join(args.save_directory,
                            'openfoam_pressureRe2000AoA35_gmshZeroGradient.png')
# into a .png
os.system('convert -append {} {} {}'.format(file_path_source_1,
                                            file_path_source_2,
                                            file_path_destination))
# into a .pdf
os.system('convert -append {} {} {}'.format(file_path_source_1,
                                            file_path_source_2,
                                            file_path_destination.replace('.png', '.pdf')))
