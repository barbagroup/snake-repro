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

time_steps = [47500, 130000, 132500, 160000]
source_paths = []
for time_step in time_steps:
  simulation.read_fields('vorticity', time_step)
  simulation.plot_contour('vorticity',
                          field_range=[-5.0, 5.0, 101],
                          time_increment=0.0004,
                          filled_contour=True,
                          view=[-1.0, -2.0, 8.0, 2.0],
                          colorbar=(True if time_step == time_steps[-1] 
                                    else False),
                          width=6.0)
  source_paths.append(os.path.join(directory,
                                   'images',
                                   'vorticity_-1.00_-2.00_8.00_2.00',
                                   'vorticity{:0>7}.png'.format(time_step)))
# create pdf
destination_path = os.path.join(os.getcwd(),
                                'petibm-0.1.1_vorticityRe2000AoA35.pdf')
os.system('pdfjam {} --nup 1x{} --outfile {}'.format(' '.join(source_paths),
                                                     len(source_paths),
                                                     destination_path))