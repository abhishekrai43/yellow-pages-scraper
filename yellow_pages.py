import sys
print sys.path
import selenium
import csv
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

search_term = input("Enter the search (Two Words at most) :")
if len(search_term.split()) > 1:
    new = search_term.split(" ")
    i = len(new[0])
    name1 = search_term[:i] + '+' + search_term[i + 1:]
    search_term = name1
location = input("Enter the City :")
header_added = False

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
url = f"https://www.yellowpages.com/search?search_terms={search_term}&geo_location_terms={location}"
def get_data():
    global header_added
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
    main_div = driver.find_element_by_css_selector('div.search-results.organic')
    rests = main_div.find_elements_by_xpath('//a[@class="business-name"]')
    cats = main_div.find_elements_by_class_name('categories')
    phones = main_div.find_elements_by_css_selector('div.phones.phone.primary')
    st_addr = main_div.find_elements_by_class_name('street-address')
    locality = main_div.find_elements_by_class_name('locality')
    for rest, cat, ph, st, lo in zip(rests, cats, phones, st_addr, locality):
        dict1 = {'Firm Name': rest.text, "Category": cat.text, "Phone Number": ph.text, "Street Address": st.text,
                 "Locality": lo.text}
        with open(f'Yellow_Pages_{search_term}_{location}.csv', 'a+', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, dict1.keys())
            if not header_added:
                w.writeheader()
                header_added = True
            w.writerow(dict1)


i = 1
get_data()
while True:
    try:
        i += 1
        url = f"https://www.yellowpages.com.au/search?search_terms={search_term}&geo_location_terms={location}&page={i}"
        get_data()
    except Exception as e:
        print("All Pages Scraped")
        driver.quit()
        break






