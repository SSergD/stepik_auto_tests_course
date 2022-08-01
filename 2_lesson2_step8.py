from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

currend_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(currend_dir, 'file.txt')

Name = browser.find_element(by="xpath", value="//input[@name='firstname']")
Name.send_keys('In')

Last_name = browser.find_element(by="xpath", value="//input[@name='lastname']")
Last_name.send_keys('Do')

Email = browser.find_element(by="xpath", value="//input[@name='email']")
Email.send_keys('gf@g.ru')

File = browser.find_element(by="xpath", value="//input[@id='file']")
File.send_keys(file_path)

Send = browser.find_element(by="xpath", value="//button[@class='btn btn-primary']").click()


