import requests

url = 'https://example.com/report.pdf'  # URL файла
response = requests.get(url)

with open('report.pdf', 'wb') as file:
    file.write(response.content)

print("Файл скачан.")












from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://example.com/register')  # URL страницы регистрации

# Заполнение формы
driver.find_element(By.NAME, 'username').send_keys('myusername')
driver.find_element(By.NAME, 'password').send_keys('mypassword')
driver.find_element(By.NAME, 'email').send_keys('myemail@example.com')

# Отправка формы
driver.find_element(By.NAME, 'submit').click()

print("Форма отправлена.")
driver.quit()














from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com/shop')  # URL интернет-магазина

products = driver.find_elements(By.CLASS_NAME, 'product')
for product in products:
    name = product.find_element(By.CLASS_NAME, 'product-name').text
    price = product.find_element(By.CLASS_NAME, 'product-price').text
    print(f'Название: {name}, Цена: {price}')

driver.quit()








from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')  # URL сайта

# Проверка кнопки "Добавить в корзину"
add_to_cart_button = driver.find_element(By.ID, 'add-to-cart')
assert add_to_cart_button.is_displayed(), "Кнопка не отображается"
add_to_cart_button.click()

print("Кнопка 'Добавить в корзину' работает.")
driver.quit()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://example.com/shop')  # URL интернет-магазина

# Прокрутка вниз до конца страницы
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Ждем загрузки новых элементов

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Сбор данных после прокрутки
products = driver.find_elements(By.CLASS_NAME, 'product')
for product in products:
    print(product.text)

driver.quit()

















import requests
from bs4 import BeautifulSoup

url1 = 'https://example.com/page1'
url2 = 'https://example.com/page2'

response1 = requests.get(url1)
response2 = requests.get(url2)

soup1 = BeautifulSoup(response1.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

data1 = soup1.find_all(class_='data-class')  # Замените на нужный класс
data2 = soup2.find_all(class_='data-class')

differences = set(data1) - set(data2)
print("Различия:", differences)















import requests
from bs4 import BeautifulSoup

url1 = 'https://example.com/page1'
url2 = 'https://example.com/page2'

response1 = requests.get(url1)
response2 = requests.get(url2)

soup1 = BeautifulSoup(response1.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

data1 = soup1.find_all(class_='data-class')  # Замените на нужный класс
data2 = soup2.find_all(class_='data-class')

differences = set(data1) - set(data2)
print("Различия:", differences)


























from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://example.com')  # URL сайта

# Проверка наличия логотипа
logo_present = len(driver.find_elements(By.ID, 'logo')) > 0
assert logo_present, "Логотип не найден"

print("Логотип присутствует на странице.")
driver.quit()




















from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get('https://example.com')  # URL сайта

# Взаимодействие со всплывающим окном
alert = Alert(driver)
