from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import chrome_driver
from pages.base_page import BasePage


class LoginPage:
    # УРЛ страницы
    URL = 'https://stellarburgers.nomoreparties.site/login'
    # форма входа
    LOGIN_FORM = (By.XPATH, ".//h2[text()='Вход']")
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//form//fieldset[1]//input")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//form//fieldset[2]//input")
    BUTTON_LOGIN = (By.XPATH, ".//form//button")

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
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(BasePage.BUTTON_ORDER))
        return 1