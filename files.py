__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
import zipfile
import re


folder = os.getcwd()
folder_cache = os.path.join(folder, 'cache')
zip_file = os.path.join(folder, 'data.zip')

# excersize 1
def clean_cache():
    check = os.listdir(folder)
    if 'cache' in check:
        #delete folder
        shutil.rmtree(folder_cache) 
    
    #create folder
    os.mkdir(folder_cache) 

# excersize 2
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder_cache)

# excersize 3
def cached_files():
    os.chdir(folder_cache)
    file_list = []
    for file in os.listdir():
        if os.path.isfile(file):
            file_path = os.path.abspath(file)
            file_list.append(file_path)
    return file_list

# excersize 4
def find_password(file_list):
    for file_name in file_list:
        with open(file_name, 'r') as file:
            for line in file:
                if 'password' in line:
                    password = re.search("(?<=\: ).*", line).group()
                    return password
