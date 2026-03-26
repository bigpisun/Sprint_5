import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    # Добавляем опцию, чтобы выбирать браузер через командную строку
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture
def driver(request):
    # Получаем имя браузера из командной строки
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        # Опция, чтобы окно было развернуто на весь экран (удобно для тестов)
        options.add_argument("--start-maximized")
        # Если нужно запускать в headless режиме (без UI) для CI, можно раскомментировать
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    
    # Устанавливаем неявное ожидание, чтобы Selenium ждал появления элементов
    driver.implicitly_wait(5)
    
    yield driver
    
    # После завершения теста закрываем браузер
    driver.quit()