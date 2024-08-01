
from conftest import chrome_driver
from data import email, password
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestAccountPage:
    def test_turn_page_with_constructor_button(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.BUTTON_CONSTRUCTOR).click()

        assert BasePage(chrome_driver).is_displayed()

    def test_turn_page_with_logo(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.LOGO).click()

        assert BasePage(chrome_driver).is_displayed()

    def test_logout(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.BUTTON_EXIT).click()

        assert LoginPage(chrome_driver).is_displayed()
