from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    send = browser.find_element_by_id("answer").send_keys(y)
    chk = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    btn = browser.find_element_by_class_name("btn").click()


finally:
    time.sleep(10)
    browser.quit()


