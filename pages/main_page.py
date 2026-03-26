from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MainPage(BasePage):
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Кнопка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    
    # Кнопка "Конструктор" - пробуем разные варианты
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[text()='Конструктор']")
    CONSTRUCTOR_BUTTON_ALT1 = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and contains(text(), 'Конструктор')]")
    CONSTRUCTOR_BUTTON_ALT2 = (By.XPATH, "//a[@href='/']")
    CONSTRUCTOR_BUTTON_ALT3 = (By.LINK_TEXT, "Конструктор")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")
    
    # Раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]")
    
    # Раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    
    # Раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]")
    
    # Активный раздел
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_personal_account(self):
        self.click_element(self.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        """Клик по кнопке Конструктор с повторными попытками"""
        try:
            # Пробуем основной локатор
            self.click_element(self.CONSTRUCTOR_BUTTON)
        except:
            try:
                # Пробуем альтернативный локатор
                self.click_element(self.CONSTRUCTOR_BUTTON_ALT1)
            except:
                try:
                    # Пробуем по ссылке
                    self.click_element(self.CONSTRUCTOR_BUTTON_ALT3)
                except:
                    # Последний вариант - по href
                    self.click_element(self.CONSTRUCTOR_BUTTON_ALT2)

    def click_logo(self):
        self.click_element(self.LOGO)

    def click_buns_section(self):
        self.click_element(self.BUNS_SECTION)

    def click_sauces_section(self):
        self.click_element(self.SAUCES_SECTION)

    def click_fillings_section(self):
        self.click_element(self.FILLINGS_SECTION)

    def get_active_section_text(self):
        return self.get_text_from_element(self.ACTIVE_SECTION)