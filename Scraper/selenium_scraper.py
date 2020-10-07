
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import json

option = webdriver.ChromeOptions()
option.add_argument(' — incognito')

# does the task without opening browser window, but something lagged
# option.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)

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

clothing_full_list = driver.find_elements_by_tag_name('article')

link_list = []
for clothing in clothing_full_list:
    elem = clothing.find_elements_by_tag_name('a')[0]
    link_list.append(elem.get_attribute('href'))

link_list = list(set(link_list))

scraped_info = []

for link in link_list:
    driver.get(link)
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "description")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()

    product_name = driver.find_elements_by_class_name('description')[0].find_elements_by_tag_name('h1')[0].text
    brand = driver.find_elements_by_class_name('brand')[0].text
    providers = driver.find_elements_by_class_name('bp-print-provider')
    provider_results = []

    for ind_prov in providers:
        provider_name = ind_prov.find_elements_by_class_name('text-ellipsis')[0].text
        items = ind_prov.find_elements_by_class_name('item')
        price = items[2].text
        shipping = items[3].text
        sizes = items[6].text
        avg_production_time = items[7].text

        provider_dict = {
            "Provider name": provider_name,
            "Price": price,
            "Shipping cost": shipping,
            "Sizes": sizes,
            "Average production time": avg_production_time
        }

        provider_results.append(provider_dict)

    product_info = {
        "Product name": product_name,
        "Brand": brand,
        "Providers": provider_results
    }

    scraped_info.append(product_info)

with open('data1.json', 'w') as output_file:
    json.dump(scraped_info, output_file)

driver.quit()

    


