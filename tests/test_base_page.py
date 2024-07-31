from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import email, password
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestBasePage:
    def test_login_with_button_login(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.BUTTON_LOGIN).click()
        WebDriverWait(chrome_driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)

    def test_login_with_button_account(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.BUTTON_ACCOUNT).click()
        WebDriverWait(chrome_driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)

    def test_go_to_profile_account(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.go_to()
        login_page.login(email, password)

        chrome_driver.find_element(*BasePage.BUTTON_ACCOUNT).click()

        assert WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(AccountPage.PROFILE_TAB))

    def test_scroll_to_sauces_from_buns(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_SAUCES).get_attribute('class')
                and chrome_driver.find_element(*BasePage.SAUCE_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.SAUCE_LIST).is_displayed())

    def test_scroll_to_filling_from_buns(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()

        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_FILLING).get_attribute('class')
                and chrome_driver.find_element(*BasePage.FILLING_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.FILLING_LIST).is_displayed())

    def test_scroll_to_buns_from_sauces(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        chrome_driver.find_element(*base_page.SECTION_BUNS).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_BUNS).get_attribute('class')
                and chrome_driver.find_element(*BasePage.BUN_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.BUN_LIST).is_displayed())

    def test_scroll_to_filling_from_sauces(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_FILLING).get_attribute('class')
                and chrome_driver.find_element(*BasePage.FILLING_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.FILLING_LIST).is_displayed())

    def test_scroll_to_buns_from_filling(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        chrome_driver.find_element(*base_page.SECTION_BUNS).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_BUNS).get_attribute('class')
                and chrome_driver.find_element(*BasePage.BUN_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.BUN_LIST).is_displayed())

    def test_scroll_to_sauce_from_filling(self, chrome_driver):
        base_page = BasePage(chrome_driver)
        base_page.go_to()
        chrome_driver.find_element(*base_page.SECTION_FILLING).click()

        chrome_driver.find_element(*base_page.SECTION_SAUCES).click()

        assert ("type_current" in chrome_driver.find_element(*base_page.SECTION_SAUCES).get_attribute('class')
                and chrome_driver.find_element(*BasePage.SAUCE_BANNER).is_displayed()
                and chrome_driver.find_element(*BasePage.SAUCE_LIST).is_displayed())
