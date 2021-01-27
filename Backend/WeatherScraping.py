#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:25:54 2019

@author: forestier

@editor: dagli, fanfan
"""

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import requests
import json
import schedule
from datetime import datetime

def webScrap():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.get("https://www.weatherlink.com/")

    usenameElement = driver.find_element_by_name("username")
    passwordElement = driver.find_element_by_name("password")

    usenameElement.send_keys('Smartuha68')
    passwordElement.send_keys('smart68')

    button = driver.find_element_by_id("submit")
    button.click()

    tables = []

    time.sleep(10)   # wait until page is loaded

    driver.find_element_by_class_name("short")
    tables = driver.find_elements_by_class_name("table")

    t1 = pd.read_html(tables[0].get_attribute('outerHTML'))[0]
    t2 = pd.read_html(tables[1].get_attribute('outerHTML'))[0]
    t3 = pd.read_html(tables[2].get_attribute('outerHTML'))[0]
    t4 = pd.read_html(tables[3].get_attribute('outerHTML'))[0]

    driver.close()
    driver.quit()

    return (t1, t2, t3, t4)

def dataClean(t1, t2, t3, t4):
    t1 = t1.replace(np.nan, '', regex=True)
    t2 = t2.replace(np.nan, '', regex=True)
    t3 = t3.replace(np.nan, '', regex=True)
    t4 = t4.replace(np.nan, '', regex=True)

    lines = []
    lines.append({"a": "", "b": "CURRENT", "c": "DAILY HIGHS",
                "d": "DAILY HIGHS TIME", "e": "DAILY LOWS", "f": "DAILY LOWS TIME"})
    for i, j in t1.iterrows():
        typ = j.get("Unnamed: 0")
        curr = j.get("Current")
        dh = j.get("Daily Highs")
        dh1 = j.get("Daily Highs.1")
        dl = j.get("SDaily Lows")
        dl1 = j.get("Daily Lows.1")

        lines.append({"a": typ, "b": curr, "c": dh, "d": dh1, "e": dl, "f": dl1})

    for i, j in t2.iterrows():
        typ = j.get("Unnamed: 0")
        curr = j.get("Current")
        dh = j.get("Daily Highs")
        dh1 = j.get("Daily Highs.1")
        dl = j.get("Daily Lows")
        dl1 = j.get("Daily Lows.1")

        lines.append({"a": typ, "b": curr, "c": dh, "d": dh1, "e": dl, "f": dl1})

    lines.append({"a": "WIND", "b": "2 MINUTES", "c": "10 MINUTES", "d": "", "e": "", "f": ""})
    for i, j in t3.iterrows():
        wind = j.get("Wind")
        two = j.get("2 Minutes")
        ten = j.get("10 Minutes")

        lines.append({"a": wind, "b": two, "c": ten, "d": "", "e": "", "f": ""})

    lines.append({"a": "RAIN & ET", "b": "RATE", "c": "STORM", "d": "DAY", "e": "MONTH", "f": "YEAR"})
    for i, j in t4.iterrows():
        rain_et = j.get("Rain & ET")
        rate = j.get("Rate")
        storm = j.get("Storm")
        day = j.get("Day")
        month = j.get("Month")
        year = j.get("Year")

        lines.append({"a": rain_et, "b": rate, "c": storm, "d": day, "e": month, "f": year})

        return lines

def apiPost(lines):
    batch = {"Batch": lines}
    response = requests.post("http://localhost:1337/meteos", json = batch)
    return response

def scraper():
    done = False
    for i in range(10):
        if(not(done)):
            print()
            print("Attempt",i + 1,"/ 10 :")
            try:
                (t1, t2, t3, t4) = webScrap()
            except Exception as e:
                print("\tWeb Scraping Exception -", datetime.now().strftime("%H:%M:%S"),":")
                print("\t\t",e)
                pass
            else:
                print("\tWeb Scraping Success -", datetime.now().strftime("%H:%M:%S"))
                try:
                    lines = dataClean(t1, t2, t3, t4)
                except Exception as e:
                    print("\tData Cleaning Exception -", datetime.now().strftime("%H:%M:%S"),":")
                    print("\t\t",e)
                    pass
                else:
                    print("\tData Cleaning Success -", datetime.now().strftime("%H:%M:%S"))
                    try:
                        response = apiPost(lines)
                    except Exception as e:
                        print("\tAPI Posting Exception -", datetime.now().strftime("%H:%M:%S"),":")
                        print("\t\t",e)
                        pass
                    else:
                        print("\tAPI Posting Success -", datetime.now().strftime("%H:%M:%S"))
                        done = True
    if(done):
        print("SUCCESS -", datetime.now().strftime("%H:%M:%S"))
        print("DATA :", response.text)
    else:
        print("FAILURE -", datetime.now().strftime("%H:%M:%S"))
    print("Waiting 15 minutes . . .")

scraper()

schedule.every(15).minutes.do(scraper)

while True:
    schedule.run_pending()
    time.sleep(1)
