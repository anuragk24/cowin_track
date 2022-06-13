from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib


for i in range(20):
    driver = webdriver.Firefox()
    driver.get('https://cowin.gov.in')
    tab_xpath = '//*[@id="mat-tab-label-0-2"]'

    tab = driver.find_element_by_xpath(tab_xpath)
    tab.click()

    state_xpath = '//*[@id="mat-select-0"]'

    state = driver.find_element_by_xpath(state_xpath)
    state.click()
    for i in range(32):
        driver.find_element_by_xpath(state_xpath).send_keys(Keys.DOWN)

    driver.find_element_by_xpath(state_xpath).send_keys(Keys.ENTER)
    time.sleep(1)
    city_xpath = '//*[@id="mat-select-2"]'

    city = driver.find_element_by_xpath(city_xpath)
    city.click()
    time.sleep(1)
    for i in range(2):
        driver.find_element_by_xpath(city_xpath).send_keys(Keys.DOWN)

    driver.find_element_by_xpath(city_xpath).send_keys(Keys.ENTER)

    button_xpath = '//*[@id="mat-tab-content-0-2"]/div/div/div[3]/button'

    button = driver.find_element_by_xpath(button_xpath)
    button.click()
    age18_xpath = '//*[@id="flexRadioDefault2"]'
    age18 = driver.find_element_by_xpath(age18_xpath)
    driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, age18_xpath))).click()

    driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)

    time.sleep(1)
    abc = driver.find_elements_by_class_name('dosetotal')
    data_list = []
    data = []
    for i, dose in enumerate(abc):
        data_list.append(dose.text)
        data.append(data_list[i].split('\n'))

    print(data)



    time.sleep(1)
    driver.quit()
    time.sleep(180)

