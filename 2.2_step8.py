from selenium import webdriver
import time
import os
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
try:
    name = browser.find_element_by_name("firstname").send_keys("alex")
    lastname = browser.find_element_by_name("lastname").send_keys("out")
    email = browser.find_element_by_name("email").send_keys("alex@")
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) #текущая папка
    print(current_dir)
    file_path = os.path.join(current_dir, '22_8.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    btn = browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()