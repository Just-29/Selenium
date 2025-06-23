import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')

url = driver.current_url
print('URL страницы', url) #Можно без переменной сразу указать атрибут driver.current_url
assert url == 'https://www.wikipedia.org/', 'Ошибка в URL'

current_title = driver.title
print('Текущий заголовок:', current_title)
assert current_title == 'Wikipedia', 'Некорректный заголовок страницы'

print(driver.page_source) #Получение исходного кода страницы. Можно присвоить переменной

time.sleep(3)

