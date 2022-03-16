# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:31:29 2022

@author: LuizF
"""

import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
import numpy as np
import cartopy as cr
import cartopy.crs as ccrs 
import os

infile = "C:\\Users\\LuizF\\Downloads\\scnLv1_repro2013_2007_002\\"
filename = "scnLv1_C002.2007.002.00.16.0008.G22.01_2013.3520_nc"


_, _, files = next(os.walk(infile))

ds = xr.open_dataset(infile + filename)
att = ds.attrs['s4max']


fig, ax = plt.subplots(figsize = (10, 6))

xvalues = ds['elevation'].values
yvalues = ds['S4'].values

ax.plot(xvalues, yvalues, color = 'k', lw = 2)
ax.set(ylabel = "S4 scintillation index", 
       xlabel = "Elevation angle of LEO-GPS link (°)", 
       title = "Radio Occutation F3/C - 01/01/2007")

attributes = ["s4max", "s4max9sec", "alt_s4max", 
              'lat_s4max', 'lon_s4max', 'lct_s4max',  
              'alttp_s4max','lattp_s4max', 'lontp_s4max', 
              'lcttp_s4max']

col_1 = -15
col_2 = -23

for num, text in enumerate(attributes):
    value = ds.attrs[text]
    base_tick = round(0.8 - (num / 10), 2)
    
    if num < (len(attributes) // 2):
        xcoord = col_1
        ycoord = base_tick
    else:
        xcoord = col_2
        ycoord = (len(attributes)//2) / 10 + base_tick
           
    ax.text(xcoord, ycoord, f"{text}: {value}" , 
            transform = ax.transData, fontsize = 18)
    
    
middle_point = (col_2 + col_1) // 2

ax.text(middle_point, 0.9, "Attributes", fontsize = 23, 
        transform=ax.transData)


plt.rcParams.update({'font.size': 15})

plt.show()