# Sample code for magnetic flux and injected helicity from inner electrode (2kV pulse)
@author: Josh0

import numpy as np
import scipy.integrate as sp
import matplotlib.pylab as plt


# The location will differ depending on where the file is located.
# I've had the least path issues typing the whole document path out from C: (on Windows)
location = 'C:\\Users\\Josh0\\Documents\\1. Josh Documents\\Graduate School - Bryn Mawr College\\Plasma Lab (BMX) Research\\Analysis\\Data\\2020\\Flux_10142020\\'
scopename = '10142020pico1\\'
filename = '20201014-0001'

# Skip however many rows in your .txt document until the data start (and headings stop)
data = np.loadtxt(location + scopename + filename + '.txt', skiprows=3, unpack=True)

"""
The .txt file for the flux data is of the form:

time (ms)           Channel A (V)   Channel B (V)   Channel C (V)   Channel D (V)
0                     ..... =>
:                     ..... =>
:                     ..... =>
446433 entries        ..... =>

Channel A: EMF outside solenoid
Channel B: EMF inside solenoid (middle)
Channel C: EMF 3 inches from gun edge
Channel D: Discharge Current
"""

# Getting the time and EMF data organized
time_ms = data[0]
time_s = time_ms*1e-3
emf_out = data[1]
emf_middle = data[2]
emf_gun_edge = data[3]

# Listing the probe diameter and area.  Here we have a 3.8" probe.
probe_diameter = 0.009652 # in meters (3.8" probe)
probe_area = np.pi*((probe_diameter/2)**2)

# We have EMF data, need to integrate to get magnetic flux data.
# Method of integration is the cumulative trapezoidal numerical integration (scipy.cumtrapz)
flux_out = sp.cumtrapz(emf_out, time_ms*1e-3)
flux_middle = sp.cumtrapz(emf_middle, time_ms*1e-3)
flux_gun_edge = sp.cumtrapz(emf_gun_edge, time_ms*1e-3)

B_out = flux_out/probe_area
B_middle = flux_middle/probe_area
B_gun_edge = flux_gun_edge/probe_area

# Now we need the injected helicity; defined as the integral of (flux*gun_voltage).
# gun_voltage was found previously (see discharge_current_voltage.py)

# Calculating the integrand first and then will integrate:
out_int_helicity_50_150us = flux_out*484.94
middle_int_helicity_50_150us = flux_middle*484.94
gunedge_int_helicity_50_150us = flux_gun_edge*484.94

out_inj_helicity_50_150 = sp.cumtrapz(out_int_helicity_50_150us, time_ms[1:]*1e-3)
middle_inj_helicity_50_150 = sp.cumtrapz(middle_int_helicity_50_150us, time_ms[1:]*1e-3)
gunedge_inj_helicity_50_150 = sp.cumtrapz(gunedge_int_helicity_50_150us, time_ms[1:]*1e-3)

# Now take our data and make some plots
# Here there are two plots that share the x axis (flux and injected helicity), and are only with middle position

fig1 (ax1,ax2) = plt.subplots(2, sharex=True)
ax1.plot(time_ms[1:]+1.5, flux_middle*1e-3, color='blue', linewidth=3)
ax1.set_ylabel(r'Flux $(mWb)$', fontsize=22)
ax1.grid(True, alpha=0.5)
ax1.tick_params(axis='x', bottom=False)
ax1.tick_params(axis='y', labelsize=20, width=1)
for axis in ['top','bottom','left','right']:
  ax1.spines[axis.set_linewidth(2)

ax2.plot(time_ms[2:]+1.5, middle_inj_helicity_50_150*1e3, color='red', linewidth=3)
ax2.set_ylabel(r'Injected Helicity $(\frac{mWb}{m^2})$', fontsize=22)
ax2.set_xlabel(r'Time $(ms)$', fontsize=22)
ax2.grid(True, alpha=0.5)
ax2.tick_params(axis='x', labelsize=20, width=1)
ax2.tick_params(axis='y', labelsize=20, width=1)
for axis in ['top','bottom','left','right']
  ax2.spines[axis.set_linewidth(2)



