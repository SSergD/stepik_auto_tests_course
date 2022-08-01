from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    sunduk =browser.find_element(By.XPATH, '//img')
    x = sunduk.get_attribute('valuex')

    #x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    #x = x_element.text
    y = calc(x)

    insert0 = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    insert0.send_keys(y)

    robot = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    robot.click()

    robot2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    robot2.click()

    submit = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
    submit.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



