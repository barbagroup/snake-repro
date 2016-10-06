"""
Computes the observed order of convergence for the temporal discretization.
"""

import os
import warnings

import numpy

import snake
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


def observed_order_of_convergence(fine, medium, coarse, ratio, order=None):
  """
  Computes the observed order of convergence using three consecutive solutions
  (fine, medium, coarse) with a given refinement ratio.
  """
  try:
    length = len(fine)
  except:
    return (numpy.log((coarse-medium)/(medium-fine))
            / numpy.log(ratio))
  return (numpy.log(numpy.linalg.norm(coarse-medium, ord=order)
                    / numpy.linalg.norm(medium-fine, ord=order))
          / numpy.log(ratio))


time_increments = ['dt=5.0E-05', 'dt=1.0E-04', 'dt=2.0E-04']
final_time_steps = [2000, 1500, 1250]
refinement_ratio = 2.0

fx, fy = [], []
p = []
qx, qy = [], []

main_directory = os.path.dirname(__file__)

for time_increment, final_time_step in zip(time_increments, final_time_steps):
  directory = os.path.join(main_directory,
                           time_increment.replace('=', ''))
  simu = CuIBMSimulation(directory=directory,
                         description=time_increment)
  simu.read_forces()
  fx.append(simu.forces[0].values[-1])
  fy.append(simu.forces[1].values[-1])
  simu.read_grid()
  p_simu = simu.read_pressure(final_time_step)
  p.append(p_simu.values)
  qx_simu, qy_simu = simu.read_fluxes(final_time_step)
  qx.append(qx_simu.values)
  qy.append(qy_simu.values)


file_path = os.path.join(os.path.dirname(__file__),
                         'temporalConvergence.txt')
with open(file_path, 'w') as outfile:
  outfile.write('\n* Drag force:\n')
  outfile.write('Value and relative difference with the reference value (smallest dt)\n')
  outfile.write('\t{}: {}\n'.format(time_increments[0], fx[0]))
  for i in (1, 2):
    outfile.write('\t{}: {} ({}%)\n'.format(time_increments[i], 
                                            fx[i], 
                                            (fx[i]-fx[0])/fx[0]*100.0))
  outfile.write('Observed order of convergence: {}\n'
                .format(observed_order_of_convergence(fx[0], fx[1], fx[2], 
                                                      refinement_ratio)))

  outfile.write('\n* Lift force:\n')
  outfile.write('Value and relative difference with the reference value (smallest dt)\n')
  outfile.write('\t{}: {}\n'.format(time_increments[0], fy[0]))
  for i in (1, 2):
    outfile.write('\t{}: {} ({}%)\n'.format(time_increments[i], 
                                            fy[i], 
                                            (fy[i]-fy[0])/fy[0]*100.0))
  outfile.write('Observed order of convergence: {}\n'
                .format(observed_order_of_convergence(fy[0], fy[1], fy[2], 
                                                      refinement_ratio)))

  outfile.write('\n* Pressure field:\n')
  outfile.write('L2-norm of the difference with the reference field (smallest dt)\n')
  outfile.write('normalized by the L2-norm of the reference field\n')
  for i in (1, 2):
    value = numpy.linalg.norm(p[i]-p[0])/numpy.linalg.norm(p[0])
    outfile.write('\t{}: {}\n'.format(time_increments[i], value))
  outfile.write('Observed order of convergence: {}\n'
                .format(observed_order_of_convergence(p[0], p[1], p[2], 
                                                      refinement_ratio)))

  outfile.write('\n* Fluxes in the x-direction:\n')
  outfile.write('L2-norm of the difference with the reference field (smallest dt)\n')
  outfile.write('normalized by the L2-norm of the reference field\n')
  for i in (1, 2):
    value = numpy.linalg.norm(qx[i]-qx[0])/numpy.linalg.norm(qx[0])
    outfile.write('\t{}: {}\n'.format(time_increments[i], value))
  outfile.write('Observed order of convergence: {}\n'
                .format(observed_order_of_convergence(qx[0], qx[1], qx[2], 
                                                      refinement_ratio)))

  outfile.write('\n* Fluxes in the y-direction:\n')
  outfile.write('L2-norm of the difference with the reference field (smallest dt)\n')
  outfile.write('normalized by the L2-norm of the reference field\n')
  for i in (1, 2):
    value = numpy.linalg.norm(qy[i]-qy[0])/numpy.linalg.norm(qy[0])
    outfile.write('\t{}: {}\n'.format(time_increments[i], value))
  outfile.write('Observed order of convergence: {}\n'
                .format(observed_order_of_convergence(qy[0], qy[1], qy[2], 
                                                      refinement_ratio)))
