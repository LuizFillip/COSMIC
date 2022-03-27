# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:06:07 2022

@author: LuizF
"""

import os.path
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from create_filename import *


def download_data(fname, output_path):
    
    """
    Web scrapy routine for data download of F3/C 
    Parameters
    ----------
        fname: String (filename)
               Create a url domain which doy (day of year) and year
               with create_filename function (see python file with same name)
        output_path:
                String (destination path)
                
               
    Download of Cosmic 1 data from: 
    https://data.cosmic.ucar.edu/gnss-ro/cosmic1/repro2013
    
    """  
    #import libraries
    import requests 
    from tqdm import tqdm
    from bs4 import BeautifulSoup 
    import time

    url = fname.url
    datatype = fname.datatype

    read_html = requests.get(url)
    s = BeautifulSoup(read_html.text, "html.parser")

    for link in s.find_all('a', href=True):
        #Find hiperlinks in html parser text
        href = link['href']
        
        #Condition for check datatype product
        if datatype in href:
            
            #Going to the hiperlink (main site + choice) 
            remote_file = requests.get(url + href)
            total_length = int(remote_file.headers.get('content-length', 0))
            chunk_size = 1024
            
            # To save to a relative path.
            #Subrotine for to do the download process itself and 
            #Add an progress bar for check the size and time of download
            with open(output_path + href, 'wb') as file, tqdm(
                    desc= "Downloading",
                    total = total_length,
                    unit='iB',
                    unit_scale = True,
                    unit_divisor = chunk_size,
            ) as bar:
                for chunk in remote_file.iter_content(chunk_size = chunk_size): 
                    if chunk: 
                        size = file.write(chunk)   
                        bar.update(size) 
                        
                
#####Tests

doy = 2
datatype = "scnLv1"
year = 2007

infile = 'C:\\Users\\LuizF\\Videos\\test\\'


# = create_filename(datatype = datatype, year = year, doy = doy)


