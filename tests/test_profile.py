import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.register_page import RegisterPage
from helpers.generators import generate_user_data
from config import BASE_URL

class TestProfile:

    @pytest.fixture
    def login_user(self, driver):
        # Регистрируем пользователя
        driver.get(BASE_URL + "register")
        register_page = RegisterPage(driver)
        user = generate_user_data()
        register_page.register(user['name'], user['email'], user['password'])
        
        # Логинимся
        driver.get(BASE_URL + "login")
        login_page = LoginPage(driver)
        login_page.login(user['email'], user['password'])
        
        yield driver, user

    def test_go_to_personal_account(self, login_user):
        driver, _ = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account()

        profile_page = ProfilePage(driver)
        assert profile_page.is_element_visible(profile_page.EXIT_BUTTON), "Не удалось перейти в личный кабинет"

    def test_go_from_profile_to_constructor_by_button(self, login_user):
        driver, _ = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account()

        profile_page = ProfilePage(driver)
        assert profile_page.is_element_visible(profile_page.EXIT_BUTTON)
        
        # Небольшая пауза для стабильности
        time.sleep(1)
        
        # Кликаем конструктор
        main_page.click_constructor()
        
        # Проверяем, что вернулись на главную
        assert main_page.is_element_visible(main_page.BUNS_SECTION), "Не удалось перейти в конструктор по кнопке"

    def test_go_from_profile_to_constructor_by_logo(self, login_user):
        driver, _ = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_element_visible(profile_page.EXIT_BUTTON)

        main_page.click_logo()
        assert main_page.is_element_visible(main_page.BUNS_SECTION), "Не удалось перейти в конструктор по логотипу"

    def test_logout(self, login_user):
        driver, _ = login_user
        main_page = MainPage(driver)
        main_page.click_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.click_exit_button()

        login_page = LoginPage(driver)
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), "Не удалось выйти из аккаунта"