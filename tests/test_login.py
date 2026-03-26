import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from helpers.generators import generate_user_data
from config import BASE_URL

class TestLogin:

    @pytest.fixture
    def create_user(self, driver):
        # ПРАВИЛЬНО: переходим на страницу регистрации
        driver.get(BASE_URL + "register")
        register_page = RegisterPage(driver)
        user = generate_user_data()
        
        # Регистрируем пользователя
        register_page.register(user['name'], user['email'], user['password'])
        
        # Возвращаем данные для входа
        yield user
        
        # Небольшая пауза после теста
        driver.implicitly_wait(2)

    def test_login_via_main_page_button(self, driver, create_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.login(create_user['email'], create_user['password'])

        assert main_page.is_element_visible(main_page.PERSONAL_ACCOUNT_BUTTON), "Не удалось войти через кнопку на главной"

    def test_login_via_personal_account_button(self, driver, create_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.login(create_user['email'], create_user['password'])

        assert main_page.is_element_visible(main_page.PERSONAL_ACCOUNT_BUTTON), "Не удалось войти через Личный кабинет"

    def test_login_via_register_form_button(self, driver, create_user):
        driver.get(BASE_URL + "register")
        register_page = RegisterPage(driver)
        register_page.click_login_link()

        login_page = LoginPage(driver)
        login_page.login(create_user['email'], create_user['password'])

        main_page = MainPage(driver)
        assert main_page.is_element_visible(main_page.PERSONAL_ACCOUNT_BUTTON), "Не удалось войти через кнопку в форме регистрации"

    def test_login_via_forgot_password_button(self, driver, create_user):
        driver.get(BASE_URL + "login")
        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()

        # На странице восстановления пароля кликаем "Войти"
        login_page.click_login_button_on_forgot_page()

        # Теперь на странице логина
        login_page.login(create_user['email'], create_user['password'])

        main_page = MainPage(driver)
        assert main_page.is_element_visible(main_page.PERSONAL_ACCOUNT_BUTTON), "Не удалось войти через кнопку в форме восстановления пароля"