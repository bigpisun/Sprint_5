from faker import Faker
import random
import string

fake = Faker()
Faker.seed(0)  # Фиксируем seed для повторяемости, если нужно

def generate_user_data():
    """
    Генерирует случайные данные для регистрации.
    Возвращает словарь: {'name': ..., 'email': ..., 'password': ...}
    """
    # Генерируем имя
    name = fake.first_name()
    
    # Генерируем email. Используем логин: имя_фамилия + рандомные цифры
    # Чтобы было уникально
    login_part = f"{name.lower()}_{fake.last_name().lower()}_{random.randint(100, 999)}"
    domain = "@test.ru"
    email = login_part + domain
    
    # Генерируем пароль. Минимум 6 символов. Для теста ошибки будем делать отдельно.
    # Обычно генерируем нормальный пароль.
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    return {
        "name": name,
        "email": email,
        "password": password
    }

def generate_invalid_password():
    """
    Генерирует пароль короче 6 символов для проверки ошибки.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))