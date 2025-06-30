import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']") #находим локатор input для dropdown

driver.get("https://demoqa.com/select-menu")

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.") #находим нужную опцию введя его текст
time.sleep(2)
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.TAB) #выбираем его отправляя enter или tab для дозавершения текста и выбора
time.sleep(3)