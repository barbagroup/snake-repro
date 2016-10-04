"""
Plots the instantaneous force coefficients obtained on three systematically 
refined grids in the uniform region (h=0.006, 0.004, and 0.00267).
The grid is stretched outside the uniform region to the external boundaries with
a constant ratio of 1.01.
We use absolute tolerances of 1.0E-16 and 1.0E-08 as exit criterion for the 
velocity and Poisson solvers, respectively.
"""

import os
import sys
import warnings

import numpy
from scipy import interpolate
from matplotlib import pyplot

import snake
from snake.cuibm.simulation import CuIBMSimulation


if snake.__version__ != '0.1.2':
  warnings.warn('The figures were originally created with snake-0.1.2, '+
                'you are using snake-{}'.format(snake.__version__))


cases = []
resolutions = ['h=0.00267', 'h=0.004', 'h=0.006']
time_limits = (1.0, 2.0)
time_step = int(6.0 / 2.0E-04)

fx, fy = [], []
p = []
qx, qy = [], []

for resolution in resolutions:
  case = CuIBMSimulation(directory=os.path.join(os.path.dirname(__file__),
                                                resolution.replace('=', '')),
                         description=resolution)
  case.read_forces()
  case.get_mean_forces(limits=time_limits)
  fx.append(case.forces[0].mean['value'])
  fy.append(case.forces[1].mean['value'])
  case.read_grid()
  p_tmp = case.read_pressure(time_step)
  p.append(p_tmp.values)
  qx_tmp, qy_tmp = case.read_fluxes(time_step)
  qx.append(qx_tmp.values)
  qy.append(qy_tmp.values)
  cases.append(case)

ratio = 1.5
order = (numpy.log((fx[2]-fx[1])/(fx[1]-fx[0]))/numpy.log(ratio))
print(order)
order = (numpy.log((fy[2]-fy[1])/(fy[1]-fy[0]))/numpy.log(ratio))
print(order)

# interpolate the pressure field from the fine grid to the coarse one
x, y = cases[0].grid[0], cases[0].grid[1]
x_p, y_p = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
f = interpolate.interp2d(x_p, y_p, p[0].transpose(), 
                         kind='cubic')
x, y = cases[-1].grid[0], cases[-1].grid[1]
x_p, y_p = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
p_f2c = f(x_p, y_p).transpose()

# interpolate the pressure field from the medium grid to the coarse one
x, y = cases[1].grid[0], cases[1].grid[1]
x_p, y_p = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
f = interpolate.interp2d(x_p, y_p, p[1].transpose(), 
                         kind='cubic')
x, y = cases[-1].grid[0], cases[-1].grid[1]
x_p, y_p = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
p_m2c = f(x_p, y_p).transpose()

a = []
for i in range(3):
  a.append(numpy.linalg.norm(p[i]) / ((cases[i].grid[0].size-1)*(cases[i].grid[1].size-1)))
order = (numpy.log((a[2]-a[1])/(a[1]-a[0]))/numpy.log(ratio))
print(order)

order = (numpy.log(numpy.linalg.norm(p[2]-p_m2c)
                   / numpy.linalg.norm(p_m2c-p_f2c))
         / numpy.log(ratio))
print(order)

pyplot.figure()
levels = numpy.linspace(0.0, 1.0, 10)
cont = pyplot.contourf(x_p, y_p, numpy.absolute(p[-1]-p_m2c),
                       levels=levels,
                       extend='both')
cbar = pyplot.colorbar(cont)
pyplot.title('coarse-medium')

pyplot.figure()
levels = numpy.linspace(0.0, 1.0, 10)
cont = pyplot.contourf(x_p, y_p, numpy.absolute(p_m2c-p_f2c),
                       levels=levels,
                       extend='both')
cbar = pyplot.colorbar(cont)
pyplot.title('medium-fine')

pyplot.figure()
levels = numpy.linspace(-0.5, 0.5, 10)
x, y = cases[0].grid[0], cases[0].grid[1]
x_p, y_p = 0.5 * (x[1:] + x[:-1]), 0.5 * (y[1:] + y[:-1])
cont = pyplot.contourf(x_p, y_p, 
                       p[0].transpose(),
                       levels=levels,
                       extend='both')
cbar = pyplot.colorbar(cont)
pyplot.title('fine')


pyplot.show()

# x = numpy.arange(-5.01, 5.01, 0.25)
# y = numpy.arange(-5.01, 5.01, 0.25)
# xx, yy = numpy.meshgrid(x, y)
# z = numpy.sin(xx**2+yy**2)
# f = interpolate.interp2d(x, y, z, kind='cubic')
# print(x.shape)
# print(y.shape)
# print(z.shape)

# xnew = numpy.arange(-5.01, 5.01, 1e-2)
# ynew = numpy.arange(-5.01, 5.01, 1e-2)
# znew = f(xnew, ynew)
# pyplot.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
# pyplot.show()

sys.exit()

# Plots the instantaneous force coefficients obtained with different meshes.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
colors = ('#377eb8', '#ff7f00', '#990026', '#002699', '#739900', '#CC0099')
for i, case in enumerate(cases):
  ax.plot(case.forces[0].times, 2.0*case.forces[0].values,
          label='$C_d$ - ${}$'.format(resolutions[i]),
          color=colors[2*i],
          linestyle='-', linewidth=1,
          zorder=10+i)
for i, case in enumerate(cases):
  ax.plot(case.forces[1].times, 2.0*case.forces[1].values,
          label='$C_l$ - ${}$'.format(resolutions[i]),
          color=colors[2*i+1],
          linestyle='-', linewidth=1,
          zorder=10+i)
ax.axis([0.0, 6.0, 0.75, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 14})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficients.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)

# Plots the instantaneous force coefficients over a smaller time-range.
fig, ax = pyplot.subplots(figsize=(6, 4))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time-unit')
ax.set_ylabel('force coefficients')
colors = ('#377eb8', '#ff7f00', '#990026', '#002699', '#739900', '#CC0099')
for i, case in enumerate(cases):
  ax.plot(case.forces[0].times, 2.0*case.forces[0].values,
          label='$C_d$ - ${}$'.format(resolutions[i]),
          color=colors[2*i],
          linestyle='-', linewidth=1,
          zorder=10+i)
for i, case in enumerate(cases):
  ax.plot(case.forces[1].times, 2.0*case.forces[1].values,
          label='$C_l$ - ${}$'.format(resolutions[i]),
          color=colors[2*i+1],
          linestyle='-', linewidth=1,
          zorder=10+i)
ax.axis([3.0, 5.0, 1.0, 3.5])
ax.legend(ncol=2, loc='upper right', prop={'size': 14})
file_path = os.path.join(os.path.dirname(__file__),
                         'forceCoefficientsZoom.png')
pyplot.savefig(file_path,
               bbox_inches='tight',
               format='png',
               dpi=300)
