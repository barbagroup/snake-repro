"""
Generates Figure 10 of the manuscript 
as a .pdf file named `petibm011_vorticityRe2000AoA35.pdf`.
"""

import os
import shutil
import yaml
import argparse
import warnings

import snake
from snake.petibm.simulation import PetIBMSimulation


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


simulation_directory = dirs['petibm011_vorticity']['Re2000AoA35']
simulation = PetIBMSimulation(directory=simulation_directory)
simulation.read_grid(file_path=os.path.join(simulation.directory, 'grid.txt'))

time_steps = [47500, 130000, 132500, 160000]
inputs = []
for time_step in time_steps:
  simulation.read_fields('vorticity', time_step)
  simulation.plot_contour('vorticity',
                          field_range=[-5.0, 5.0, 101],
                          time_increment=0.0004,
                          view=[-1.0, -2.0, 8.0, 2.0],
                          colorbar=(True if time_step == time_steps[-1] 
                                    else False),
                          width=6.0,
                          dpi=300,
                          style='snakeReproducibility')
  # copy .png file here
  file_path_source = os.path.join(simulation.directory,
                                  'images',
                                  'vorticity_-1.00_-2.00_8.00_2.00',
                                  'vorticity{:0>7}.png'.format(time_step))
  file_path_destination = os.path.join(args.save_directory,
                                       'petibm011_vorticity{}Re2000AoA35.png'
                                       .format(time_step))
  shutil.copy(file_path_source, file_path_destination)
  inputs.append(file_path_destination)

# create single .pdf page with pdfjam
file_path_out = os.path.join(args.save_directory,
                             'petibm011_vorticityRe2000AoA35.pdf')
os.system('pdfjam {} --nup 1x{} --outfile {}'.format(' '.join(inputs),
                                                     len(inputs),
                                                     file_path_out))
