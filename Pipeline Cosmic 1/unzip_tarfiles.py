# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:18:20 2022

@author: LuizF
"""

def unzip_tarfiles(output_path):
    
    """
    Unzip tar files will extract all files from the '.tar.gz' file 
    in another directory 
    (will use os libray for create a new directory with the same name).
    
    WARNINGS! Input_path is the output_path (from download data routine). 
    Parameters
    ----------
        É o caminho de entrada onde o arquivo tar.gz
        It is the input path which there is tar.gz. file
        
    """

    import os
    from tqdm import tqdm
    import tarfile
    
    
    #Find files in directroy 
    for chunk in next(os.walk(output_path), 
                      (None, None, []))[2]:
        
        #If find the file 
        if '.tar.gz' in chunk:
            
            #Path where is the tarfile
            some_source = output_path + chunk
            
            try:
                #Create a name for a directory with the same name of 
                # .tar.gz file (downloaded)
                NewFolderName = chunk.replace('.tar.gz', '')
                
                # Use function 'mkdir' for create a new directory
                newfolder_path = output_path + NewFolderName
                os.mkdir(newfolder_path)
                
                #conditions for the folder created 
            except OSError:
                #For the case of directory already exists
                print(f"Creation of the directory {NewFolderName} failed")
            else:
                pass
            
            #open tar file 
            with tarfile.open(some_source) as zf:
                
                # Go over each member and add a progress bar
                for member in tqdm(iterable = zf.getmembers(), 
                                   total=len(zf.getmembers()), 
                                   desc='Extracting'):
                
                    # Extract each member into new folder already created
                    zf.extract(member=member, path = newfolder_path)
            
            #Finally remove the .tar.gz file (to avoid memory overload)
            os.remove(some_source)

output_path = "C:\\Users\\LuizF\\Videos\\test\\"