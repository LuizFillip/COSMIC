import os
import datetime as dt
import xarray as xr
import datetime as dt
from GEO import quick_map
import os
import xarray as xr

infile = "D:\\ionPrf_repro2013_2013_001\\"
files = os.listdir(infile)

out = []



filename = files[0]



def datetime_from_file(filename) -> dt.datetime:
    """Return date from year and doy"""
    _, year, doy, hour, minute, _, _ = tuple(filename.split("."))
    date = dt.date(int(year), 1, 1) + dt.timedelta(int(doy) - 1)
    time = dt.time(int(hour), int(minute))
    return dt.datetime.combine(date, time)

for filename in files:
    

    date_time = datetime_from_file(filename)

    if ((date_time > dt.datetime(2013, 1, 1, 20, 20)) and
        (date_time < dt.datetime(2013, 1, 1, 20, 50))):
        
        ds = xr.open_dataset(os.path.join(infile, filename))

        lon_s = ds.attrs["edmaxlon"]

        if lon_s < -30 and (lon_s > -90):
            lat_lims = dict(min = -45, max = 45, stp = 15)
            lon_lims = dict(min = -90, max = -30, stp = 30) 
            
            fig, ax = quick_map(lat_lims = lat_lims, 
            lon_lims = lon_lims)
            ax.set(title = date_time)
            ax.scatter(ds["GEO_lon"], ds["GEO_lat"], c = ds["ELEC_dens"])
        
        

