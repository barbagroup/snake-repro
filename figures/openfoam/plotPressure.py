# file: plotPressure.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D pressure fields
#              and cats the png files into a pdf page.


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

# create pdf
images_directory = os.path.join(directory, 
                                'images', 
                                'pressure_-2.00_-3.00_15.00_3.00')
names = ['pressure052.00.png', 'pressure053.00.png']
source_paths = [os.path.join(images_directory, name) for name in names]
destination_path = os.path.join(os.getcwd(),
                                'openfoam_pressureRe2000AoA35_gmshZeroGradient.pdf')
os.system('pdfjam {} --nup 1x{} --outfile {}'.format(' '.join(source_paths),
                                                     len(source_paths),
                                                     destination_path))
