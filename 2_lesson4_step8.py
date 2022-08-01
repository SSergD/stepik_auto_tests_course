from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html//h5[@id='price']"), "$100")
    )
browser.find_element(by=By.ID, value="book").click()

browser.execute_script("window.scrollBy(0, 250);")

x = browser.find_element(By.XPATH, "/html//span[@id='input_value']").text
y = str(math.log(abs(12 * math.sin (int(x)) ) ))

z = browser.find_element(By.XPATH, "/html//input[@id='answer']").send_keys(y)

w = browser.find_element(By.XPATH, "//button[@id='solve']")
w.click()