from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
try:
    btn = browser.find_element_by_class_name("btn").click()
    alert = browser.switch_to_alert()
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    btn2 = browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(10)
    browser.quit()