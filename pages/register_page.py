from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


class RegisterPage:
    # УРЛ страницы
    URL = 'https://stellarburgers.nomoreparties.site/register'
    # форма регистрации
    RESITER_FORM = (By.XPATH, ".//h2[text()='Регистрация']")
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, ".//form//fieldset[1]//input")
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//form//fieldset[2]//input")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//form//fieldset[3]//input")
    # Кнопка регистрации
    REGISTER_BUTTON = (By.XPATH, ".//form//button")
    # Ошибка некорректного пароля
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(text(), 'пароль') and contains(@class, 'error')]")
    # Кнопка "Войти"
    BUTTON_LOGIN = (By.XPATH, ".//a[contains(@href, '/login')]")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.RESITER_FORM))

    def register(self, name, email, password):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.REGISTER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

    def error_massage_is_displayed(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(RegisterPage.PASSWORD_ERROR))
        return 1

    def click_button_login(self):
        self.driver.find_element(*RegisterPage.BUTTON_LOGIN).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))
