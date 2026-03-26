from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    # Кнопка "Выход" в личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    def click_exit_button(self):
        self.click_element(self.EXIT_BUTTON)