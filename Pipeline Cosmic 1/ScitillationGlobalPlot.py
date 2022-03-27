# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cartopy as cr
import cartopy.crs as ccrs
 

dumb = []

for num in range(1, 5):

    infile = f"C:\\Users\\LuizF\\Videos\\test\\2007\\00{num}.txt"
    
    dumb.append(pd.read_csv(infile, delim_whitespace = True))
    
df = pd.concat(dumb)

df.index = pd.to_datetime(df['datetime'])
df = df.replace(-999.0, np.nan)
df = df.dropna()

#Get of equatorial scitillations, so polar scintillation events were excluded
geo_cond = ((df['lattp_s4max'] < 50) & (df['lattp_s4max'] > -50)) 

#For to avoid the influences from the E region and the noisier 
#information from the GPS-RO profiles above 600 km.
alt_cond = ((df['alttp_s4max'] > 150) & (df['alttp_s4max'] < 600))
s4_cond = (df['s4max'] >= 0.3)

#df = df.loc[ geo_cond & s4_cond & alt_cond, :]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()

ax.coastlines()

lat = df['lat_s4max'].values
lon = df['lon_s4max'].values
values = df['s4max9sec'].values

cmap = ax.scatter(lon, lat, s = 5,  c = values, cmap = 'jet')

plt.colorbar(cmap)

ax.set(xticks = np.arange(-180, 190, 30), xlabel = "Longitude (°)",
       yticks = np.arange(-90, 100, 20), ylabel = "Latitude (°)")

plt.show()