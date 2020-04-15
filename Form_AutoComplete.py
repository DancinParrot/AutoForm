import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date

browser = webdriver.Edge('C:/Users/kaizh/Downloads/msedgedriver.exe')
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSc8Gm2HKnrSGxAD3NVWi7wPQXgYVKsVs6fnLojxDY20gXqRFg/viewform')

indexno = '23'
today = date.today()

#values of the form
input_Date = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
input_Index = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
input_Class = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]'
Class_4E1 = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[3]'
Feeling = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div'
Acknowledgement = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div/label/div/div[1]/div'

submit_but = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div'

def sleep():
    time.sleep(3)

i = 0
while i < 1:
    browser.find_element_by_xpath(input_Date).send_keys(today.strftime('%d/%m/%Y'))
    browser.find_element_by_xpath(input_Index).send_keys(indexno)
    browser.find_element_by_xpath(Feeling).click()
    browser.find_element_by_xpath(Acknowledgement).click()
    sleep()
    browser.find_element_by_xpath(input_Class).click()
    sleep()
    browser.find_element_by_xpath(Class_4E1).click()
    sleep()
    browser.find_element_by_xpath(submit_but).click()

    i += 1

    sleep()
    browser.back()
    sleep()

print('Form completed.')
