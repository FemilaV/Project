# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time
import pandas as pd

# connecting chrome driver to the GDACS website
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gdacs.org/About/overview.aspx")
print(driver.title)

# Finding the link_text for alerts in the website
link = driver.find_element_by_link_text("ALERTS")
link.click()

# Finding search, autofilling the checkboxes for different types of disasters
# Filling the from date, to date and country'India'  and clicking the submit button
# Scrapping all the result to a list
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Search"))
    )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChEq"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChTs"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChFl"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChTc"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChVo"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChDr"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputChFf"))
    )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputDateFrom"))
    )
    element.clear()
    element.send_keys("2000-10-10")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputDateTo"))
    )
    element.clear()
    element.send_keys("2021-10-10")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputCountry"))
    )
    element.clear()
    element.send_keys("India")

    element = WebDriverWait(driver, 10).until(  
        EC.presence_of_element_located((By.ID, "btnsearch"))
    )
    element.click()

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[@class='generic_search']"))
    )
    data = []
    for row in table.find_elements_by_xpath(".//tr"):
        for td in row.find_elements_by_xpath(".//td[@style='text-align:left;']"):
            a = td.text
            data.append(a)
    #print(data)
except:
    driver.quit()

# creating two list disaster and date from scrapped data 
disaster = []
date = []
for x in range(len(data)):
    if x%2 ==0:
        disaster.append(data[x])
    else:
        date.append(data[x])
#print("-"*50)
#print(disaster)
#print(date)

final = zip(date,disaster)

# Transfer the data to a spreadsheet
wb = Workbook()
wb['Sheet'].title = 'GDCS'
sh1 = wb.active
sh1.append(['date','disaster'])
for x in list(final):
    sh1.append(x)
wb.save("Project.csv")



                
        












