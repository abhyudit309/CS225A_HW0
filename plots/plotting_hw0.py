#!/usr/bin/env python3

# read text files and plot them

import matplotlib.pyplot as plt
import numpy as np
import sys
import math

# data file to read 
file_name_e1 = "../data_files/q2-e-i.txt"
file_name_e2 = "../data_files/q2-e-ii.txt"
file_name_f1 = "../data_files/q2-f-i.txt"
file_name_f2 = "../data_files/q2-f-ii.txt"
file_name_g = "../data_files/q2-g.txt"

mass_e1 = np.loadtxt(file_name_e1, skiprows=0)
mass_e2 = np.loadtxt(file_name_e2, skiprows=0)
grav_f1 = np.loadtxt(file_name_f1, skiprows=0)
grav_f2 = np.loadtxt(file_name_f2, skiprows=0)
grav_g = np.loadtxt(file_name_g, skiprows=0)


q3_dense = np.linspace(-90,90,251)
q3 = (-90, -60, -30, 0, 30, 60, 90)

d2_dense = np.linspace(0,2,251)
d2 = (0, 0.5, 1, 1.5, 2)

d4_dense = np.linspace(0,2,251)
d4 = (0, 0.5, 1, 1.5, 2)

# plotting
plt.figure(1)
for i in range(mass_e1.shape[1]):
  plt.plot(q3_dense, mass_e1[:, i])
plt.xlabel('$\\theta_3$ (degrees) $\\rightarrow$')
plt.ylabel('$m_{11}$, $m_{22}$, $m_{33}$ $\\rightarrow$')
plt.legend(['$m_{11}$', '$m_{22}$', '$m_{33}$'])
plt.title('Plot of $m_{11}$, $m_{22}$, $m_{33}$ versus $\\theta_3$')
plt.grid()
plt.show()

plt.figure(2)
for i in range(mass_e2.shape[1]):
  plt.plot(d2_dense, mass_e2[:, i])
plt.xlabel('$d_2$ (metres) $\\rightarrow$')
plt.ylabel('$m_{11}$, $m_{22}$, $m_{33}$ $\\rightarrow$')
plt.legend(['$m_{11}$', '$m_{22}$', '$m_{33}$'])
plt.title('Plot of $m_{11}$, $m_{22}$, $m_{33}$ versus $d_2$')
plt.grid()
plt.show()

plt.figure(3)
for i in range(grav_f1.shape[1]):
  plt.plot(q3_dense, grav_f1[:, i])
plt.xlabel('$\\theta_3$ (degrees) $\\rightarrow$')
plt.ylabel('$G_1$, $G_2$, $G_3$ $\\rightarrow$')
plt.legend(['$G_1$', '$G_2$', '$G_3$'])
plt.title('Plot of $G_1$, $G_2$, $G_3$ versus $\\theta_3$')
plt.grid()
plt.show()

plt.figure(4)
for i in range(grav_f2.shape[1]):
  plt.plot(d2_dense, grav_f2[:, i])
plt.xlabel('$d_2$ (metres) $\\rightarrow$')
plt.ylabel('$G_1$, $G_2$, $G_3$ $\\rightarrow$')
plt.legend(['$G_1$', '$G_2$', '$G_3$'])
plt.title('Plot of $G_1$, $G_2$, $G_3$ versus $d_2$')
plt.grid()
plt.show()

plt.figure(5)
for i in range(grav_g.shape[1]):
  plt.plot(d4_dense, grav_g[:, i])
plt.xlabel('$d_4$ (metres) $\\rightarrow$')
plt.ylabel('$G_1$, $G_2$, $G_3$, $G_4$ $\\rightarrow$')
plt.legend(['$G_1$', '$G_2$', '$G_3$', '$G_4$'])
plt.title('Plot of $G_1$, $G_2$, $G_3$, $G_4$ versus $d_4$')
plt.grid()
plt.show()