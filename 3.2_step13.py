from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "name")]')
        input1.send_keys("Alexander")
        input2 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "last")]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "email")]')
        input3.send_keys("AlexP@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,"Should be Congratulations!")

    def tes_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "name")]')
        input1.send_keys("Alexander")
        input2 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "last")]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath(
            '//input[contains(@class, "form-control") and contains(@placeholder, "email")]')
        input3.send_keys("AlexP@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be Congratulations!")


if __name__ == '__main__':
    unittest.main()
