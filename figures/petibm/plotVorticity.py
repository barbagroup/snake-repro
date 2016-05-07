# file: plotVorticity.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Plots the 2D vorticity field.
# Run this script from the simulation directory.


import os

from snake.petibm.simulation import PetIBMSimulation


directory = os.path.join(os.environ['HOME'],
                         'simulations_PetIBM',
                         'flyingSnake',
                         '2d',
                         'cuibmGrid',
                         'velocityBiCGStabPoissonBiCGStab',
                         'flyingSnake2dRe2000AoA35_20160426')
simulation = PetIBMSimulation(directory=directory)
simulation.read_grid()

for time_step in [130000, 132500, 160000]:
  simulation.read_fields('vorticity', time_step)
  simulation.plot_contour('vorticity',
                          field_range=[-5.0, 5.0, 101],
                          time_increment=0.0004,
                          filled_contour=True,
                          view=[-1.0, -2.0, 8.0, 2.0],
                          width=6.0)
  source_path = os.path.join(directory,
                'images',
                'vorticity_-1.00_-2.00_8.00_2.00',
                'vorticity{:0>7}.png'.format(time_step))
  destination_path = os.path.join(os.getcwd(),
                                  'petibm-0.1.1_vorticity{:0>7}Re2000AoA35.pdf'
                                  ''.format(time_step))
  os.system('convert {} {}'.format(source_path, destination_path))