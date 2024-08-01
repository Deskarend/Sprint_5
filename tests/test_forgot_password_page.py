from data import email, password
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


class TestForgotPassword:
    def test_login_with_button_login(self, chrome_driver):
        forgot_page = ForgotPasswordPage(chrome_driver)
        forgot_page.go_to()

        forgot_page.click_button_login()

        login_page = LoginPage(chrome_driver)
        assert login_page.login(email, password)
