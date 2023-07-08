# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:10:37 2022

@author: LuizF
"""

class create_filename:
    
    """
    Create filename with informations of 
    F3/C (FormaSat 3/ Cosmic 1) products
    from 
    
    Parameters
    ----------
    _datatype: String
        F3/C Product post-processed data for the levels 1b and 2.
        Defoult scnLv1 (Scintillation)
    year: integer
        The availability of dataset on the website is 2006-04-22 to 
        2014-04-30 for F3/C post-processed data. Defoult: 2007
    doy: integer
        Day of year (1 to 365). Defoult: 001
    
    Returns 
    -------
   
    """
    
    def __init__(self, datatype = "scnLv1", year = 2007, doy = 1):
        
        self.datatype_ = datatype
        self.year = int(year)
        self.doy = int(doy)
        
        #DOY sanity conditions
        if self.doy < 1 or self.doy > 365:
            raise ValueError("Doy (day of year) must be between 1 to 365")
        
        if self.doy < 10:
            doy_text = f"00{doy}"
            
        elif self.doy > 10 and self.doy < 100:
            doy_text = f"0{doy}"
    
        else:
            doy_text = f"{doy}"
            
        #Products list
        level1b = ["atmPhs", "gpsBit", "ionPhs", "leoClk", 
                "leoOrb", "podTec", "scnLv1"] 
    
        level2 = ["atmPrf", "bfrPrf", "echPrf", "eraPrf", 
                 "gfsPrf", "ionPrf", "wetPrf"]
        
        if (self.datatype_ in level1b):
            level = "level1b"
        elif (self.datatype_ in level2):
            level = "level2"
        else:
            raise ValueError(f"The datatype must be level1b" /
                             "{level1b} or level2: {level2}")
        self.doy_text = doy_text    
        self.domain = "https://data.cosmic.ucar.edu/gnss-ro/cosmic1/repro2013/"
        self.fname = f"{datatype}_repro2013_{year}_{self.doy_text}.tar.gz"
        self.url_ = f"{level}/{year}/{self.doy_text}/" 
    
    @property    
    def folder_tar(self):    
        return self.fname 
    @property    
    def datatype(self):    
        return self.datatype_ 
    @property
    def folder(self):
        return self.fname.replace('.tar.gz', '')
    @property 
    def url(self):
        return self.domain + self.url_
    @property 
    def filename(self):
        return self.doy_text + ".txt"
    
####Testss    
doy = 2
datatype = "scnLv1"

fname = create_filename(datatype = datatype, doy = doy)
#print(fname.url)