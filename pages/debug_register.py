from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.education-services.ru/register")
time.sleep(2)

# Найдем все поля ввода
inputs = driver.find_elements(By.TAG_NAME, "input")
for i, inp in enumerate(inputs):
    print(f"Поле {i}:")
    print(f"  type={inp.get_attribute('type')}")
    print(f"  name={inp.get_attribute('name')}")
    print(f"  placeholder={inp.get_attribute('placeholder')}")
    print(f"  class={inp.get_attribute('class')}")
    print()

time.sleep(3)
driver.quit()