# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 14:41:36 2022

@author: ravjy
"""

import requests
import zipfile
import os
import glob

download_url = 'https://msedgedriver.azureedge.net/100.0.1185.29/edgedriver_win64.zip'

req = requests.get(download_url)

#print(req.headers)

filename = req.url[download_url.rfind('/')+1:]
#print(filename)

# Writing the downloaded file as Binary
try:
    with open(filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Driver successfully downloaded in Working Directory")

except IOError:
    print("File not downloaded, Please check")
except FileNotFoundError:
    print("File not found, Please check")
except EOFError:
    print("End of the file. Please check")
except ImportError:
    print("Can not find the file. Please check")


working_directory = os.getcwd()
#print(working_directory)

# Picking the latest file from the explorer
try:
    username = os.environ.get("USERNAME")
    downloads_folder = "{0}\\*".format(working_directory)
except OSError:
    print("Operating System error")
    
#print(downloads_folder)

# Getting the details of latest file available in downloads folder
try:
    list_of_files = glob.glob(downloads_folder)
    latest_file = max(list_of_files, key=os.path.getmtime)
    #print(latest_file)
except IsADirectoryError:
    print("Please check the directory")

           
# Unzipping the downloaded package

#latest_file = r"C:\Users\ravjy\edgedriver_win64.zip"

with zipfile.ZipFile(latest_file, 'r') as zip_ref:
    zip_ref.extractall(working_directory)

    
# Killing the Zip file

try:
    os.remove(latest_file)
except OSError:
    print("Unable to kill the file")
except FileNotFoundError:
    print("Unable to locate the file to kill")

