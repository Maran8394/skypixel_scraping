from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from excel_writer import excel_write

s = Service(executable_path="C:/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.skypixel.com/users/merrwatson/followers")

SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
count = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    print(count)
    count += 1

chosen_image = driver.find_elements(By.CLASS_NAME, "_2ou6")
for count, a in enumerate(chosen_image):
    link = a.get_attribute('href')
    if link != "None":
        l = link.split("https://").pop()
        excel_write(file_name="links", write_list=[str(l)])
    else:
        pass
