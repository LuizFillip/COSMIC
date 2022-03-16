# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:50:48 2022

@author: LuizF
"""

import os

path_to_dir  = 'C:\\Users\\Desktop\\temp'  # path to directory you wish to remove

def delete_folder(path_to_dir):
    files_in_dir = os.listdir(path_to_dir)     # get list of files in the directory
    
    for file in files_in_dir:                  # loop to delete each file in folder
        os.remove(f'{path_to_dir}/{file}')     # delete file
    
    os.rmdir(path_to_dir) 