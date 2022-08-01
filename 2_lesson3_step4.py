from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

Button = browser.find_element(by="xpath", value="//button")
Button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, 'input_value').text
y = str(math.log(abs(12 * math.sin (int(x)) ) ))

z = browser.find_element(By.ID, 'answer')
z.send_keys(y)

Submit = browser.find_element(by="xpath", value="//button[@class='btn btn-primary']").click()


