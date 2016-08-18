"""
Generates Figure 5 of the paper 
as a .pdf file named `ibamr_vorticityRe2000AoA35.pdf`.
"""


import os
import shutil
import yaml
import argparse
import warnings

import snake
from snake.ibamr.simulation import IBAMRSimulation


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

# plot vorticity field at state 56 (about 61 time-units)
# of the simulation using a traction-free outlet condition
simulation_directory = dirs['ibamr_vorticityRe2000AoA35']['tractionFreeOutlet']
simulation = IBAMRSimulation(directory=simulation_directory)
simulation.plot_field_contours_visit('vorticity', (-5.0, 5.0),
                                     body='flyingSnake2dAoA35ds004',
                                     solution_folder='numericalSolution',
                                     view=(-2.0, -5.0, 15.0, 5.0),
                                     width=1000,
                                     states=(56, 57, 1))
file_path_in_1 = os.path.join(simulation.directory, 
                               'images', 
                               'vorticity_-2.00_-5.00_15.00_5.00',
                               'vorticity0000056.png')

# plot vorticity field at state 52 (about 61 time-units)
# of the simulation using a traction-free outlet condition
# augmented by a stabilized outlet condition
simulation_directory = dirs['ibamr_vorticityRe2000AoA35']['stabilizedOutlet']
simulation = IBAMRSimulation(directory=simulation_directory)
simulation.plot_field_contours_visit('vorticity', (-5.0, 5.0),
                                     body='flyingSnake2dAoA35ds004',
                                     solution_folder='numericalSolution',
                                     view=(-2.0, -5.0, 15.0, 5.0),
                                     width=1000,
                                     states=(52, 53, 1))
file_path_in_2 = os.path.join(simulation.directory, 
                               'images', 
                               'vorticity_-2.00_-5.00_15.00_5.00',
                               'vorticity0000052.png')

# convert the two .png files into one
file_path_out = os.path.join(args.save_directory, 'ibamr_vorticityRe2000AoA35.png')
os.system('convert -append {} {} {}'.format(file_path_in_1,
                                            file_path_in_2,
                                            file_path_out))
# convert the two .png files into a single .pdf
os.system('convert -append {} {} {}'.format(file_path_in_1,
                                            file_path_in_2,
                                            file_path_out.replace('.png', '.pdf')))
