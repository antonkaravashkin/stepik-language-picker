from selenium.webdriver.common.by import By
from conftest import browser

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


def test_user_should_see_add_bucket_button(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
