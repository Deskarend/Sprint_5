from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import email, password
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


class TestForgotPassword:
    def test_login_with_button_login(self, chrome_driver):
        forgot_page = ForgotPasswordPage(chrome_driver)
        forgot_page.go_to()

        chrome_driver.find_element(*forgot_page.BUTTON_LOGIN).click()
        WebDriverWait(chrome_driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)
