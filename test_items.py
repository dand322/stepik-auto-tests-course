import time
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_add_button_exist(browser):
    try:
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".btn-add-to-basket1")
        time.sleep(10)
        btn = True
    except NoSuchElementException:
        print('Zero element for U!')
        btn = False
    assert btn, "Кнопка не найдена"

