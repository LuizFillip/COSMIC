# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:46:46 2022

@author: LuizF
"""

def get_attrs(infile, fname, set_limit = None): 
    
    import xarray as xr
    import pandas as pd
    from tqdm import tqdm 
    import os
    
    directory = infile + fname.folder
    _, _, files = next(os.walk(directory))
    

    #Interest parameters that is will use for analysis
    output_attrs = {"datetime": [], "s4max": [], "s4max9sec":[],
                    "alt_s4max": [], 'lat_s4max':[], 'lon_s4max':[], 
                    'lct_s4max':[],  'alttp_s4max':[],'lattp_s4max':[],
                    'lontp_s4max':[], 'lcttp_s4max':[]}
    if set_limit:
        files = files[set_limit[0]:set_limit[1]]
    
        
    for num in tqdm(range(len(files)), desc='Getting atributes'):
    
        try:
            #Use xarray for read netCDF files
            complete_path = f"{directory}\\{files[num]}" 
            
            ds = xr.open_dataset(complete_path)
            #get atributes from dataset
            att = ds.attrs
            #construct with datetime function
            from datetime import datetime 
            
            #Construct a variable 
            _datetime_values = datetime(int(att['year']), int(att['month']),
                                         int(att['day']), int(att['hour']), 
                                         int(att['minute']), int(att['second']))
    
            #extract datetime values
            output_attrs['datetime'].append(_datetime_values)
            #pick up the parameters of interest
            parameters = ["s4max", "s4max9sec", "alt_s4max", 
                          "lat_s4max", "lon_s4max", "lct_s4max",  
                          "alttp_s4max","lattp_s4max", "lontp_s4max", 
                          "lcttp_s4max"]
            
            #Loop for extract interest parameters and add into dictionary
            for name in parameters:
                output_attrs[name].append(att[name])
                
        except:
            print(f"{num}: The filename {files[num]} doens't works!")
    
    df = pd.DataFrame(output_attrs)
    
    try:
        year_folder = f"{infile}\\{att['year']}"
        os.mkdir(year_folder)
        #conditions for the folder created 
    except OSError:
        #For the case of directory already exists
        pass
    else:
        pass
        
   
    df.to_csv(f"{year_folder}\\{fname.filename}", sep = ' ')
    


  




