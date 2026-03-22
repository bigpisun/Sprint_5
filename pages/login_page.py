from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Поле Email на странице логина
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Поле Пароль
    PASSWORD_INPUT = (By.NAME, "Пароль")
    
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    
    # Кнопка "Войти" на странице восстановления пароля
    LOGIN_BUTTON_FORGOT_PAGE = (By.XPATH, "//a[contains(text(), 'Войти')]")

    def login(self, email, password):
        """Метод для входа в аккаунт"""
        self.send_keys_to_element(self.EMAIL_INPUT, email)
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def click_register_link(self):
        """Клик по ссылке 'Зарегистрироваться'"""
        self.click_element(self.REGISTER_LINK)

    def click_forgot_password_link(self):
        """Клик по ссылке 'Восстановить пароль'"""
        self.click_element(self.FORGOT_PASSWORD_LINK)
    
    def click_login_button_on_forgot_page(self):
        """Клик по кнопке 'Войти' на странице восстановления пароля"""
        self.click_element(self.LOGIN_BUTTON_FORGOT_PAGE)