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

        login_page = LoginPage(chrome_driver)
        login_page.login(email, password)

        BasePage(chrome_driver).click_button_account_after_login()

        assert chrome_driver.find_element(*AccountPage.ACCOUNT_NAME).get_attribute('value') == name

    def test_register_with_invalid_password(self, chrome_driver):
        register_page = RegisterPage(chrome_driver)
        register_page.go_to()

        name = helper.get_random_name()
        email = helper.get_random_email()
        password = '12'

        register_page.register_try(name, email, password)

        assert register_page.error_massage_is_displayed()

    def test_login_with_button_login(self, chrome_driver):
        register_page = RegisterPage(chrome_driver)
        register_page.go_to()

        register_page.click_button_login()

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)
