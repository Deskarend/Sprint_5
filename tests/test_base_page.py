from conftest import chrome_driver

from data import email, password
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestBasePage:
    def test_login_with_button_login(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        base_page.click_button_login()

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)

    def test_login_with_button_account(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        base_page.click_button_account_before_login()

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)

    def test_go_to_profile_account(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.go_to()
        login_page.login(email, password)

        chrome_driver.find_element(*BasePage.BUTTON_ACCOUNT).click()

        assert AccountPage(chrome_driver).is_displayed()

    def test_scroll_to_sauces_from_buns(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        assert base_page.sauces_is_displayed()

    def test_scroll_to_filling_from_buns(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        assert base_page.filling_is_displayed()

    def test_scroll_to_buns_from_sauces(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        chrome_driver.find_element(*base_page.SECTION_BUNS).click()

        assert base_page.buns_is_displayed()

    def test_scroll_to_filling_from_sauces(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        assert base_page.filling_is_displayed()

    def test_scroll_to_buns_from_filling(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        chrome_driver.find_element(*base_page.SECTION_BUNS).click()

        assert base_page.buns_is_displayed()

    def test_scroll_to_sauce_from_filling(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        assert base_page.sauces_is_displayed()
