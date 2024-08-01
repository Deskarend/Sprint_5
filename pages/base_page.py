from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # УРЛ страницы
    URL = 'https://stellarburgers.nomoreparties.site/'
    # Кнопка "Войти в аккаунт"
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(text(), 'в аккаунт')]")
    # Картинки ингредиентов
    IMG_INGREDIENTS = (By.XPATH, ".//img")
    # Кнопка "Личный кабинет"
    BUTTON_ACCOUNT = (By.XPATH, ".//a[contains(@href, '/account')]")
    # Кнопка "Оформить заказ"
    BUTTON_ORDER = (By.XPATH, ".//button[contains(text(),'заказ')]")
    # Раздел "Булки"
    SECTION_BUNS = (By.XPATH, ".//span[contains(text(), 'Булки')]/parent::div")
    # Заголовок списка булок
    BUN_BANNER = (By.XPATH, ".//h2[contains(text(), 'Булки')]")
    # Список
    BUN_LIST = (By.XPATH, ".//*[contains(@class, 'ingredients')]//ul[1]")
    # Раздел "Соусы"
    SECTION_SAUCES = (By.XPATH, ".//span[contains(text(), 'Соусы')]/parent::div")
    # Заголовок списка соусов
    SAUCE_BANNER = (By.XPATH, ".//h2[contains(text(), 'Соусы')]")
    # Список
    SAUCE_LIST = (By.XPATH, ".//*[contains(@class, 'ingredients')]//ul[2]")
    # Раздел "Начинки"
    SECTION_FILLING = (By.XPATH, ".//span[contains(text(), 'Начинки')]/parent::div")
    # Заголовок списка начинок
    FILLING_BANNER = (By.XPATH, ".//h2[contains(text(), 'Начинки')]")
    # Список
    FILLING_LIST = (By.XPATH, ".//*[contains(@class, 'ingredients')]//ul[3]")

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(self.IMG_INGREDIENTS))

    def is_displayed(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(BasePage.IMG_INGREDIENTS))
        self.driver.find_element(*BasePage.BUTTON_ORDER)
        return 1
