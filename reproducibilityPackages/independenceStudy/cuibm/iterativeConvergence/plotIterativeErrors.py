"""
Plots the iterative errors in the forces, flux fields, and pressure fields.
"""

import os
import warnings

import numpy
from matplotlib import pyplot

import snake
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))

atol_min, atol_max = 5, 16
time_step = 1500

main_directory = os.path.dirname(__file__)

reference_directory = os.path.join(main_directory,
                                   'atol16')
reference = CuIBMSimulation(directory=reference_directory,
                            description='atol=1.0E-16')
reference.read_forces()
fx_reference = reference.forces[0].values[-1]
fy_reference = reference.forces[1].values[-1]
reference.read_grid()
p_reference = reference.read_pressure(time_step)
qx_reference, qy_reference = reference.read_fluxes(time_step)

fx_errors, fy_errors = [], []
p_errors = []
qx_errors, qy_errors = [], []

for atol in range(atol_min, atol_max):
  directory = os.path.join(main_directory,
                           'atol{}'.format(atol))
  simu = CuIBMSimulation(directory=directory,
                         description='1.0E-{}'.format(atol))
  simu.read_forces()
  fx = simu.forces[0].values[-1]
  fy = simu.forces[1].values[-1]
  simu.read_grid()
  p = simu.read_pressure(time_step)
  qx, qy = simu.read_fluxes(time_step)

  p_errors.append(numpy.linalg.norm(p.values - p_reference.values))
  qx_errors.append(numpy.linalg.norm(qx.values - qx_reference.values))
  qy_errors.append(numpy.linalg.norm(qy.values - qy_reference.values))
  fx_errors.append(numpy.abs(fx - fx_reference))
  fy_errors.append(numpy.abs(fy - fy_reference))

# Writes the errors in a .txt file.
file_path = os.path.join(os.path.dirname(__file__), 'iterativeErrors.txt')
with open(file_path, 'w') as outfile:
  outfile.write('# atol, fx, fy, p, qx, qy\n')
  atols = [10.0**-atol for atol in range(atol_min, atol_max)]
  for data in zip(atols, fx_errors, fy_errors, p_errors, qx_errors, qy_errors):
    for d in data:
      outfile.write('{}\t'.format(d))
    outfile.write('\n')

# Plots the errors in the forces, pressure field, and fluxes fields with respect
# to the reference solution.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('absolute tolerance of the Poisson solver')
ax.set_ylabel('errors')
atols = [10.0**-atol for atol in range(atol_min, atol_max)]
colors = ('#377eb8', '#ff7f00', '#990026', '#002699', '#739900', '#CC0099')
ax.loglog(atols, fx_errors,
            label='$|f_x - f_{x_{\mathtt{ref}}}|$',
            linewidth=2, linestyle='-', marker='o',
            color=colors[0],
            zorder=10)
ax.loglog(atols, fy_errors,
            label='$|f_y - f_{y_{\mathtt{ref}}}|$',
            linewidth=2, linestyle='-', marker='o',
            color=colors[1],
            zorder=10)
ax.loglog(atols, p_errors,
            label='$L_2(p - p_{\mathtt{ref}})$',
            linewidth=2, linestyle='-', marker='o',
            color=colors[2],
            zorder=10)
ax.loglog(atols, qx_errors,
            label='$L_2(q_x - q_{x_{\mathtt{ref}}})$',
            linewidth=2, linestyle='-', marker='o',
            color=colors[3],
            zorder=10)
ax.loglog(atols, qy_errors,
            label='$L_2(q_y - q_{y_{\mathtt{ref}}})$',
            linewidth=2, linestyle='-', marker='o',
            color=colors[4],
            zorder=10)
pyplot.gca().invert_xaxis()
ax.legend(ncol=1, loc='upper right', prop={'size': 12})
file_path = os.path.join(os.path.dirname(__file__),
                         'iterativeErrors.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
