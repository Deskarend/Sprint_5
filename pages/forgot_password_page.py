from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


class ForgotPasswordPage:
    # УРЛ страницы
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    # форма входа
    FORGOT_PASSWORD_FORM = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    # Кнопка "Войти"
    BUTTON_LOGIN = (By.XPATH, ".//a[contains(@href, '/login')]")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.FORGOT_PASSWORD_FORM))

    def click_button_login(self):
        self.driver.find_element(*ForgotPasswordPage.BUTTON_LOGIN).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))
