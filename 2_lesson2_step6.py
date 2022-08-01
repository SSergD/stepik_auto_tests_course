from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element(By.ID, 'input_value').text
    y = str(math.log(abs(12 * math.sin (int(x)) ) ))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 150);")

    z = browser.find_element(By.ID, 'answer')
    z.send_keys(y)

    w = browser.find_element(By.ID, 'robotCheckbox').click()

    q = browser.find_element(By.ID, 'robotsRule').click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()