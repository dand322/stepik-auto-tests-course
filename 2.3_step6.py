from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
try:
    btn1 = browser.find_element_by_class_name("btn").click()
    browser.switch_to_window(browser.window_handles[1])
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)
    btn2 = browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(10)
    browser.quit()