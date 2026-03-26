from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        """Клик по элементу"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys_to_element(self, locator, keys):
        """Ввод текста в поле"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(keys)

    def get_text_from_element(self, locator):
        """Получение текста элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        """Проверка видимости элемента"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False