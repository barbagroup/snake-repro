# file: plotPressure.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D pressure field.


import os

from snake.openfoam.simulation import OpenFOAMSimulation


directory = os.path.join(os.environ['HOME'],
                         'simulations_OpenFOAM',
                         'flyingSnake2d',
                         '2012',
                         'flyingSnake2dRe2000AoA35_20121226')
simulation = OpenFOAMSimulation(directory=directory)
simulation.plot_field_contours_paraview('pressure',
                                        field_range=(-1.0, 0.5),
                                        view=(-2.0, -3.0, 15.0, 3.0),
                                        times=(52.0, 53.0, 1.0),
                                        width=600,
                                        colormap='viridis')

images_directory = os.path.join(directory, 
                                'images', 
                                'pressure_-2.00_-3.00_15.00_3.00')
file_names_source = ['pressure052.00.png', 'pressure053.00.png']
file_names_destination = ['openfoam_pressure52Re2000AoA35_gmshZeroGradient.pdf',
                          'openfoam_pressure53Re2000AoA35_gmshZeroGradient.pdf']
for source, destination in zip(file_names_source, file_names_destination):
  os.system('convert {} {}'.format(os.path.join(images_directory, source),
                                   os.path.join(os.getcwd(), destination)))
