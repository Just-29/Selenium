import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('''указать URL для перехода''')
time.sleep('''указать время в секундах''')
driver.back()
driver.forward()
driver.refresh()
driver.current_url #Получение URL
driver.title #Получение названия страницы
driver.page_source #получение исходного кода страницы