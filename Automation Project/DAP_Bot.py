# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:50:05 2022

@author: ravjy
"""
# Importing the relevant libraries

import time
from selenium import webdriver
import os
import glob
import zipfile
import warnings
warnings.filterwarnings('ignore')

# Using the below code to capture the username

working_directory = os.getcwd()
username = os.environ.get("USERNAME")
downloads_folder = "{0}\\".format(working_directory)
# print(downloads_folder)

# ************* BOT to download the files ********************

# Estimated time to run:- 10 Seconds

# Running the BOT by using the Edge web driver
# Edge Version - Version 100.0

try:
    driver = webdriver.Edge(executable_path = "{0}\\msedgedriver.exe".format(downloads_folder))
except:
    print("Please check the driver and try again")
# The exception raised here is SessionNotCreatedException but except clause is not recognizing it.

#print("Please check the edge browser version and try again")

# Opening the link of our dataset from Kaggle
try:
    driver.get("https://www.kaggle.com/datasets/sripaadsrinivasan/indian-railways-dataset")
except NameError:
    print("Driver object is not created, please check the driver directory")
# Clicking the download button

# Waiting for the elements to load in the HTML
try:
    driver.implicitly_wait(10)
    #kaggle_button = driver.find_element(by=By.CLASS_NAME, value="sc-gVFcvn tMYCk sc-eyJofK ifWJUs")
    kaggle_button1 = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[4]/div[3]/div[2]/div/div[1]/div/a/button")
    kaggle_button1.click()
    
    driver.implicitly_wait(3)
    
    # BOT to click on the email button to sign in
    
    email_button = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div/div[2]/a/li/div")
    #print(email_button)
    email_button.click()
    
    driver.implicitly_wait(3)
    
    # BOT is entering the dummy username
    
    user_name = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div[1]/div/label/input")
    user_name.send_keys("supageek@rediffmail.com")
    
    # BOT is entering dummy password
    
    pwd = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div[2]/div/label/input")
    pwd.send_keys("P@ssw0rd899$")
    
    # BOT is clicking on the sign in button on our behalf
    
    sign_in = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div[3]/button")
    sign_in.click()
    
    # BOT is downloading the file
    
    download_btn = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[4]/div[3]/div[2]/div/div[1]/div/a/button")
    download_btn.click()
    
    # =============================================================================
    # def download_wait(path):
    #     seconds = 0
    #     dl_wait = True
    #     while dl_wait and seconds < 20:
    #         time.sleep(1)
    #         dl_wait = False
    #         for fname in os.listdir(path):
    #             #if fname.endswith('.crdownload'):
    #             if fname.startswith('archive'):
    #                 dl_wait = True
    #         seconds += 1
    #     return seconds
    # =============================================================================
    
    # BOT will wait for 6 seconds before closing the browser focous window.
    # Within 6 seconds the file download should complete.
    
    time.sleep(6)
    
    # BOT is closing the browser
    
    driver.close()
    driver.quit()

except:
    print("BOT is not running, please check.")

# Unzipping the extracted zip file dataset to current Jupyter Notebook working directory

# Finding the working directory

working_directory = os.getcwd()
#print(working_directory)
username = os.environ.get("USERNAME")
downloads_folder = "C:/Users/{0}/Downloads/*".format(username)
#print(downloads_folder)
# Checking the latest file downloaded
list_of_files = glob.glob(downloads_folder)
latest_file = max(list_of_files, key=os.path.getmtime)
#print(latest_file)
# unzipping the file to the Python working directory
try:
    with zipfile.ZipFile(latest_file, 'r') as zip_ref:
            zip_ref.extractall(working_directory)
            print("Files unzipped successfully in the working directory!")
except NameError:
    print("Unable to locate the file to unzip.")





