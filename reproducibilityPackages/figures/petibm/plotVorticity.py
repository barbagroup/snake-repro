# file: plotVorticity.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D vorticity fields,
#              copies each .png file here,
#              and merges .png files into one .pdf page.


import os
import sys
import shutil

from matplotlib import pyplot
pyplot.style.use(os.path.join(os.environ['SNAKE'], 'snake', 'styles',
                              'snakeReproducibility.mplstyle'))

import snake
from snake.petibm.simulation import PetIBMSimulation


print('\nPython version:\n{}'.format(sys.version))
print('\nsnake version: {}\n'.format(snake.__version__))

simulation = PetIBMSimulation(directory=os.path.join(os.environ['HOME'],
                                                     'snakeReproducibilityPackages',
                                                     'petibm',
                                                     'exactMarkers',
                                                     'Re2000AoA35'))
simulation.read_grid()

time_steps = [47500, 130000, 132500, 160000]
source_paths = []
for time_step in time_steps:
  simulation.read_fields('vorticity', time_step)
  simulation.plot_contour('vorticity',
                          field_range=[-5.0, 5.0, 101],
                          time_increment=0.0004,
                          view=[-1.0, -2.0, 8.0, 2.0],
                          colorbar=(True if time_step == time_steps[-1] 
                                    else False),
                          width=6.0,
                          dpi=300)
  source_paths.append(os.path.join(simulation.directory,
                                   'images',
                                   'vorticity_-1.00_-2.00_8.00_2.00',
                                   'vorticity{:0>7}.png'.format(time_step)))
  # copy .png file here
  shutil.copy(source_paths[-1], 
              'petibm011_vorticity{}Re2000AoA35.png'.format(time_step))

# create single .pdf page with pdfjam
destination_path = os.path.join(os.getcwd(),
                                'petibm011_vorticityRe2000AoA35.pdf')
os.system('pdfjam {} --nup 1x{} --outfile {}'.format(' '.join(source_paths),
                                                     len(source_paths),
                                                     destination_path))
