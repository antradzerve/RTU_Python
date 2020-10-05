
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import dbm
import time

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')
driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=option)

driver.get('https://printify.com/app/products')

SCROLL_PAUSE_TIME = 10

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    #at some point the page stops loading if it is scrolled down to max. hence the additional scroll up-down - to re-trigger loading
    driver.execute_script("window.scrollTo(0, 200);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "preview-price")))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

clothing_full_list = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div[2]/div/div/div[2]')

elems = clothing_full_list.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))

# for elem in elems:
#     new_elem = elem.get_attribure("href")
#     new_elem.click()
    


