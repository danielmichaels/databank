#!/usr/bin/env python
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def main():
    login()
    tips()

def login():
    driver.get('https://www.sportsbet.com.au/')
    driver.find_element_by_xpath('//*[@id="fakeusername"]').click()
    time.sleep(1)
    username = driver.find_element_by_xpath('//*[@id="username"]')
    username.send_keys(os.getenv('USERNAME'))
    driver.find_element_by_xpath('//*[@id="fakepassword"]').click()
    time.sleep(1)
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(os.getenv('PASSWORD'))
    driver.find_element_by_css_selector('#login-btn-ctn > a:nth-child(1)').click()

def tips():
    driver.get('https://www.sportsbet.com.au/tipping/')
    # driver.find_element_by_xpath('//*[@id="sbm-page-wrapper"]/section/a[3]')
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    main()
