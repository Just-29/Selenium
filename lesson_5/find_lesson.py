import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

'''Способы поиска эквивалентные By.***:
➖ ID = "id"
➖ XPATH = "xpath"
➖ NAME = "name"
➖ CLASS_NAME = "class name"
➖ CSS_SELECTOR = "css selector"'''

driver.get('https://www.freeconferencecall.com/ru')
time.sleep(5)


driver.find_element('id', 'signupbutton').click() #Поиск элемента и клик по нему
time.sleep(5)