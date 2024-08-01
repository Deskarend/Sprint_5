from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    # УРЛ страницы
    URL = 'https://stellarburgers.nomoreparties.site/login'
    # форма входа
    LOGIN_FORM = (By.XPATH, ".//h2[text()='Вход']")
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.LOGIN_FORM))

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        from pages.base_page import BasePage
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(BasePage.BUTTON_ORDER))
        return 1

    def is_displayed(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))
        return 1
