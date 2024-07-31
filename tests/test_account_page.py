from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import email, password
from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestAccountPage:
    def test_turn_page_with_constructor_button(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.BUTTON_CONSTRUCTOR).click()

        assert (WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(BasePage.IMG_INGREDIENTS))
                and chrome_driver.find_element(*BasePage.BUTTON_ORDER))

    def test_turn_page_with_logo(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.LOGO).click()

        assert (WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(BasePage.IMG_INGREDIENTS))
                and chrome_driver.find_element(*BasePage.BUTTON_ORDER))

    def test_logout(self, chrome_driver):
        account_page = AccountPage(chrome_driver)
        account_page.go_to(email, password)

        chrome_driver.find_element(*account_page.BUTTON_EXIT).click()

        assert WebDriverWait(chrome_driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))
