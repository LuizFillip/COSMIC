# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:15:08 2022

@author: LuizF
"""

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from create_filename import *
from download_data import *
from unzip_tarfiles import *
from get_atributes import *
from delete_folder import *

#Scintillation datatype
datatype = "scnLv1"
#year 
year = 2007

infile = 'C:\\Users\\LuizF\\Videos\\test\\'

#The loop for days must start in 1 for
for doy in range(1, 5):
    
    print(f"Running: {doy}/{year}")
    
    #Class for create a filename, url, folder name 
    fname = create_filename(datatype = datatype, year = year, doy = doy)
    
    #Scrapy of data from CDAA
    download_data(fname, output_path = infile)
    
    #unzip, create an folder and delete the '.tar.gz' folder
    unzip_tarfiles(infile)
    
    #Get the atributes of all RO files (NetCDF) 
    #Which appoint the informations about maximum values S4
    get_attrs(infile, fname)
    
    # Delete the last folder     
    delete_folder(infile + fname.folder)