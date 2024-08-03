from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AccountPage:
    # УРЛ страницы
    URL = "https://stellarburgers.nomoreparties.site/account"
    # Вкладка профиля
    PROFILE_TAB = (By.XPATH, ".//a[contains(@href,'profile')]")
    # Поле имени
    ACCOUNT_NAME = (By.XPATH, ".//input[1]")
    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    # Лого
    LOGO = (By.XPATH, ".//div[contains(@class, 'logo')]")
    # Кнопка "Выход"
    BUTTON_EXIT = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, email, password):
        self.driver.get(self.URL)
        from pages.login_page import LoginPage
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(LoginPage.LOGIN_FORM))

        self.driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPage.BUTTON_LOGIN).click()
        from pages.base_page import BasePage
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(BasePage.BUTTON_ORDER))

        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(self.PROFILE_TAB))
        return self.driver

    def is_displayed(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(AccountPage.PROFILE_TAB))
        return self.driver
