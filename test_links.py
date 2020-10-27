
import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_class_name("textarea").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    message = browser.find_element_by_class_name("smart-hints__hint")
    wrong = message.text
    assert "Correct!" in message.text, wrong
