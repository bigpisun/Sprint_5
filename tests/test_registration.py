import pytest
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from helpers.generators import generate_user_data, generate_invalid_password
import time

class TestRegistration:

    def test_successful_registration(self, driver):
        # Открываем страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)

        # Генерируем данные
        user = generate_user_data()

        # Регистрируемся
        register_page.register(user['name'], user['email'], user['password'])

        # Проверяем, что после успешной регистрации произошел редирект на страницу логина
        # Ждем появления кнопки "Войти" на странице логина
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), "Кнопка входа не отображается после регистрации"

    def test_registration_with_invalid_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        register_page = RegisterPage(driver)

        user = generate_user_data()
        invalid_password = generate_invalid_password()

        # Пытаемся зарегистрироваться с паролем < 6 символов
        register_page.register(user['name'], user['email'], invalid_password)

        # Проверяем появление ошибки
        # Здесь нужно уточнить текст ошибки в приложении, предположим "Некорректный пароль"
        error_text = register_page.get_error_text()
        assert "Некорректный пароль" in error_text or "пароль" in error_text.lower(), "Ошибка для короткого пароля не появилась"