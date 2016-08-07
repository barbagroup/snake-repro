# file: plotPressure.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D pressure fields,
#              copies the .png files here,
#              and creates one .pdf page with the images.


import os
import sys
import shutil

import snake
from snake.openfoam.simulation import OpenFOAMSimulation


print('\nPython version:\n{}'.format(sys.version))
print('\nsnake version: {}\n'.format(snake.__version__))

directory = os.path.join(os.environ['HOME'],
                         'snakeReproducibilityPackages',
                         'openfoam',
                         'gmsh',
                         'Re2000AoA35')
simulation = OpenFOAMSimulation(directory=directory)
simulation.plot_field_contours_paraview('pressure',
                                        field_range=(-1.0, 0.5),
                                        view=(-2.0, -3.0, 15.0, 3.0),
                                        times=(52.0, 53.0, 1.0),
                                        width=600,
                                        colormap='viridis')

# locate images of interest
images_directory = os.path.join(simulation.directory, 
                                'images', 
                                'pressure_-2.00_-3.00_15.00_3.00')
file_names = ['pressure052.00.png', 'pressure053.00.png']
source_paths = [os.path.join(images_directory, name) for name in file_names]
# copy .png files here
destination_paths = [os.path.join(os.getcwd(), 
                                  'openfoam_pressure52Re2000AoA35_gmshZeroGradient.png'),
                     os.path.join(os.getcwd(), 
                                  'openfoam_pressure53Re2000AoA35_gmshZeroGradient.png')]
for s, d in zip(source_paths, destination_paths):
  shutil.copy(s, d)
# convert .png files into one .pdf page with pdfjam
destination_path = os.path.join(os.getcwd(),
                                'openfoam_pressureRe2000AoA35_gmshZeroGradient.pdf')
os.system('pdfjam {} --nup 1x{} --landscape --outfile {}'.format(' '.join(source_paths),
                                                                 len(source_paths),
                                                                 destination_path))
