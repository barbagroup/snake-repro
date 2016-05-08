# file: plotVorticity.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D vorticity field,
#              copy .png file in same folder,
#              and converts .png into one .pdf page.


import os
import shutil

from snake.openfoam.simulation import OpenFOAMSimulation


directory = os.path.join(os.environ['HOME'],
                         'simulations_OpenFOAM',
                         'flyingSnake2d',
                         '2012',
                         'flyingSnake2dRe2000AoA35_20121226')
simulation = OpenFOAMSimulation(directory=directory)
simulation.plot_field_contours_paraview('vorticity',
                                        field_range=(-5.0, 5.0),
                                        view=(-5.0, -8.0, 10.0, 2.0),
                                        times=(52.0, 52.0, 1.0),
                                        width=600,
                                        colormap='RdBu_r')

images_directory = os.path.join(directory, 
                                'images', 
                                'vorticity_-5.00_-8.00_10.00_2.00')
file_name_source = 'vorticity052.00.png'
file_name_destination = 'openfoam_vorticity52Re2000AoA35_gmshZeroGradient.pdf'
# copy the .png file
shutil.copy(os.path.join(images_directory,
                         file_name_source), 
            os.path.join(os.getcwd(), 
                         file_name_destination.replace('.pdf', '.png')))
# convert into .pdf file
os.system('convert {} {}'.format(os.path.join(images_directory, file_name_source),
                                 os.path.join(os.getcwd(), file_name_destination)))
