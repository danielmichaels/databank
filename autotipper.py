#!/usr/bin/env python
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def main():
    test()

def test():
    # driver.implicitly_wait(3)
    # driver.maximize_window()
    driver.get('https://www.sportsbet.com.au/')

    driver.find_element_by_xpath('//*[@id="fakeusername"]').click()
    time.sleep(1)
    username = driver.find_element_by_xpath('//*[@id="username"]')
    # username = driver.find_element_by_id("username")
    # username.clear()

    username.send_keys("TEST")

    driver.find_element_by_xpath('//*[@id="fakepassword"]').click()
    time.sleep(1)
    password = driver.find_element_by_xpath('//*[@id="password"]')

    password.send_keys('assword')
    driver.quit()


if __name__ == '__main__':
    main()
