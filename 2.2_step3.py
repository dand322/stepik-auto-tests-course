from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

try:
    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    z = str(int(x)+int(y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
    btn = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()

