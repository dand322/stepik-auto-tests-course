from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_css_selector("#robotsRule")
    radio.click()
    send = browser.find_element_by_css_selector(".btn")
    send.click()
finally:
    time.sleep(10)
    browser.quit()