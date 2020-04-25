import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#initialise webdriver
browser = webdriver.Edge('C:/Users/kaizh/Downloads/msedgedriver.exe')
#link to form
browser.get('https://docs.google.com/forms/d/e/~~/viewform')

#your input to for the form
Name = "Test"

#xPaths of the form components here
input_Name = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
DropDown = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div[1]/div[1]/div[1]'
DropDownOption = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div[2]/div[3]'
CheckBox = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/label/div/div[1]'
RadioBut = '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div'

#xPath of the submit button of the form
submit_but = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div'

#Selenium will find the components of the form via their respective xPaths and do the necessary actions
browser.find_element_by_xpath(input_Name).send_keys(Name)
browser.find_element_by_xpath(CheckBox).click()
browser.find_element_by_xpath(RadioBut).click()
#Sometimes, Selenium will enter the input too fast which may result in the script ending prematurely
time.sleep(3)
browser.find_element_by_xpath(DropDown).click()
time.sleep(1)
browser.find_element_by_xpath(DropDownOption).click()
time.sleep(3)
browser.find_element_by_xpath(submit_but).click()

time.sleep(3)
browser.quit()
    
print('Form completed.')
