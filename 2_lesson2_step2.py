from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    summ = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))

    submit = browser.find_element(By.XPATH, '//button[@type]').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()