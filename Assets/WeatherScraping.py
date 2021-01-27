#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:25:54 2019

@author: forestier
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.weatherlink.com/")

usenameElement = driver.find_element_by_name("username")
passwordElement = driver.find_element_by_name("password")

usenameElement.send_keys('Smartuha68')
passwordElement.send_keys('smart68')

button = driver.find_element_by_id("submit")
button.click()

time.sleep(5) # wait to be sure the page is loaded

tables = []
tables = driver.find_elements_by_class_name("table")

t1 = pd.read_html(tables[0].get_attribute('outerHTML'))[0]
t2 = pd.read_html(tables[1].get_attribute('outerHTML'))[0]
t3 = pd.read_html(tables[2].get_attribute('outerHTML'))[0]
t4 = pd.read_html(tables[3].get_attribute('outerHTML'))[0]

print(t1,"\n",t2,"\n",t3,"\n",t4)