from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helper
from data import password, email
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestRegisterPage:
    def test_successful_register(self, chrome_driver):
        register_page = RegisterPage(chrome_driver)
        register_page.go_to()

        name = helper.get_random_name()
        email = helper.get_random_email()
        password = helper.get_random_password()

        register_page.register(name, email, password)
        WebDriverWait(chrome_driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        login_page = LoginPage(chrome_driver)
        login_page.login(email, password)

        chrome_driver.find_element(*BasePage.BUTTON_ACCOUNT).click()
        WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(AccountPage.PROFILE_TAB))

        assert chrome_driver.find_element(*AccountPage.ACCOUNT_NAME).get_attribute('value') == name

    def test_register_with_invalid_password(self, chrome_driver):
        register_page = RegisterPage(chrome_driver)
        register_page.go_to()

        name = helper.get_random_name()
        email = helper.get_random_email()
        password = '12'

        register_page.register(name, email, password)

        assert WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(register_page.PASSWORD_ERROR))

    def test_login_with_button_login(self, chrome_driver):
        register_page = RegisterPage(chrome_driver)
        register_page.go_to()

        chrome_driver.find_element(*register_page.BUTTON_LOGIN).click()
        WebDriverWait(chrome_driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)
