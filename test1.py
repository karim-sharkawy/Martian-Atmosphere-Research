#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:23:00 2022

@author: Karim Mohamed El-Sharkawy
"""
import numpy as np
from scipy.io import netcdf
import matplotlib.pyplot as plt

# read in the file, and the three dimensional data is stored in z
filename="c:\\Users\\karim\\OneDrive\\Desktop\\summer_research\\week 1\\Z500_ens1.nc"
f = netcdf.netcdf_file(filename,'r')
z = f.variables['z500t42']
time = f.variables['time'].data
lat = f.variables['lat'].data
lon = f.variables['lon'].data
f.close()

ii=1 # here ii is the index for the time

# now let us plot the pattern of the first day
plt.figure(1)
plt.contourf(lon,lat,z[ii,:,:],cmap='RdBu_r');
plt.colorbar()
plt.title('Z500 day (global):'+str(ii))
plt.xlabel('longitude')
plt.ylabel('latitude')

plt.figure(2)
plt.contourf(lon,lat,z[ii,:,:],cmap='RdBu_r');
plt.colorbar()
plt.title('Z500 day (regional):'+str(ii))
plt.xlim([100, 280])
plt.ylim([20, 70])
plt.xlabel('longitude')
plt.ylabel('latitude')

plt.savefig("test1.png")