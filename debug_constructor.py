from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.education-services.ru/")
time.sleep(2)

print("=== Поиск кнопки 'Конструктор' ===\n")

# Найдем все ссылки
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Всего ссылок на странице: {len(links)}\n")

for i, link in enumerate(links):
    text = link.text
    href = link.get_attribute('href')
    class_name = link.get_attribute('class')
    if text and ('Конструктор' in text or 'конструктор' in text):
        print(f"НАЙДЕНА ССЫЛКА 'Конструктор':")
        print(f"  текст: '{text}'")
        print(f"  href: '{href}'")
        print(f"  class: '{class_name}'")
        print(f"  id: '{link.get_attribute('id')}'")
        print()

# Альтернатива: поиск по XPath
print("\n=== Поиск по XPath ===")
try:
    constr = driver.find_element(By.XPATH, "//a[contains(text(), 'Конструктор')]")
    print(f"Найдено через XPath: текст='{constr.text}', href='{constr.get_attribute('href')}'")
except:
    print("XPath //a[contains(text(), 'Конструктор')] не сработал")

try:
    constr = driver.find_element(By.XPATH, "//a[contains(@class, 'header') and contains(text(), 'Конструктор')]")
    print(f"Найдено через XPath с классом: текст='{constr.text}'")
except:
    print("XPath с классом не сработал")

time.sleep(3)
driver.quit()