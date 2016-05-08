# file: plotVorticity.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D vorticity field
#              and saves it as .png and .pdf files.


import os
import shutil

from snake.ibamr.simulation import IBAMRSimulation


simulation_directory = os.path.join(os.environ['HOME'],
                                    'simulations_IBAMR',
                                    'flyingSnake2d',
                                    'discretizedBoundary',
                                    'flyingSnake2dRe2000AoA35_20150717')

simulation = IBAMRSimulation(directory=simulation_directory)

simulation.plot_field_contours_visit('vorticity', (-5.0, 5.0),
                                     body='flyingSnake2dAoA35ds004',
                                     solution_folder='numericalSolution',
                                     view=(-2.0, -5.0, 15.0, 5.0),
                                     width=600,
                                     states=(56, 57, 1))

file_path_source = os.path.join(simulation.directory, 
                               'images', 
                               'vorticity_-2.00_-5.00_15.00_5.00',
                               'vorticity0000056.png')
# copy .png file here
file_name_destination = 'ibamr_vorticity56Re2000AoA35_zeroGradientOutlet.png'
shutil.copy(file_path_source, file_name_destination)
# copy as .pdf here
file_name_destination = 'ibamr_vorticity56Re2000AoA35_zeroGradientOutlet.pdf'
os.system('convert {} {}'.format(file_path_source, file_name_destination))
