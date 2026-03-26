from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class RegisterPage(BasePage):
    # Поле "Имя" (первое поле с name="name")
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    
    # Поле "Email" (второе поле с name="name")
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    
    # Поле "Пароль"
    PASSWORD_INPUT = (By.NAME, "Пароль")
    
    # Кнопка регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    
    # Сообщение об ошибке
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

    def register(self, name, email, password):
        """Метод для регистрации нового пользователя"""
        # Вводим имя
        self.send_keys_to_element(self.NAME_INPUT, name)
        
        # Вводим email
        self.send_keys_to_element(self.EMAIL_INPUT, email)
        
        # Вводим пароль
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        
        # Нажимаем кнопку регистрации
        self.click_element(self.REGISTER_BUTTON)

    def get_error_text(self):
        """Получение текста ошибки"""
        return self.get_text_from_element(self.ERROR_MESSAGE)
    
    def click_login_link(self):
        """Клик по ссылке 'Войти' на странице регистрации"""
        self.click_element(self.LOGIN_LINK)