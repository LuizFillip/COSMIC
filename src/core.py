
import datetime as dt
from GEO import quick_map
import os
import xarray as xr
from datetime import datetime 
import pandas as pd


def get_data(ds):
    df = ds.to_dataframe()
    
    df = df.loc[(df.index > 200) & (df.index < 500)]
    
    att = ds.attrs
    
    dn = datetime(
        int(att['year']), 
        int(att['month']),
        int(att['day']), 
        int(att['hour']), 
        int(att['minute']), 
        int(att['second'])
        )
    
    df["time"] = dn
    
    return df

infile = "D:\\ionPrf_repro2013_2013_001\\"
files = os.listdir(infile)

out = []

for filename in files:
    print("running", filename)
    out.append(get_data(
        xr.open_dataset(os.path.join(infile, filename)))
        )


df = pd.concat(out)#.to_csv("cosmic.txt")



start = dt.datetime(2013, 1, 1, 0, 0)
for dn in pd.date_range(
            start, 
            start + dt.timedelta(
            hours = 23, 
            minutes = 50), freq = "10min"):
    
    df1 = df.loc[(df["time"] > dn) & 
                 (df["time"] < dn + 
                  dt.timedelta(minutes = 10))]
    
    l = df1["GEO_lon"].values[0]
    
    if l< -30:

    
        lat_lims = dict(min = -90, max = 90, stp = 15)
        lon_lims = dict(min = -180, max = 180, stp = 30) 
        
        fig, ax = quick_map(lat_lims = lat_lims, 
        lon_lims = lon_lims)
        ax.set(title = dn )
        ax.scatter(df1["GEO_lon"], df1["GEO_lat"], c = df1["ELEC_dens"])
    
#%%

print()