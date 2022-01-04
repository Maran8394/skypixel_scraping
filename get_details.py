import csv
from itertools import chain

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from excel_writer import excel_write

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

s = Service(executable_path="C:/SeleniumDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)


def mainpage(url=None):
    try:
        final_list = []
        social_links = []
        # base_url = "https://www.skypixel.com/users/djiuser-ncjznsn8uorg"
        base_url = "https://" + url[0]
        driver.get(base_url)
        driver.implicitly_wait(3)
        followers = driver.find_elements(By.CLASS_NAME, '_1VZU')
        assert followers[1].text != '0'
        name = driver.find_element(By.CLASS_NAME, '_2fgO').text
        final_list.append(name)
        s_links = driver.find_elements(By.CLASS_NAME, "vV_P")
        try:
            contry = driver.find_element(By.CLASS_NAME, "flag-icon")
            hover = ActionChains(driver).move_to_element(contry)
            hover.perform()
            flag = driver.find_element(By.CLASS_NAME, "rc-tooltip-inner").text
            flag = flag
        except NoSuchElementException:
            flag = None

        for link in s_links:
            l = link.get_attribute('href')
            social_links.append(l)
        final_list.append(flag)
        final_list.append(followers[1].text)

        to_write = list(chain([base_url], final_list, social_links))

        print(to_write)
        excel_write(write_list=to_write, file_name="datas")
        return

    except AssertionError:
        return


def links_reader():
    given_file_name = f"links/links.csv"
    try:
        with open(given_file_name, 'r+', newline='', encoding="ISO-8859-1", errors='ignore') as read_file:
            reader_writer = csv.reader((line.replace('\0', '') for line in read_file))
            for c, i in enumerate(reader_writer):
                print(c, "Iteration")
                mainpage(i)

    except Exception as e:
        print(e)


links_reader()
# mainpage()
