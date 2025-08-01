import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys #для работы с клавиатурой

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

KEYBOARD_INPUT = ("xpath", "//input[@id='target']")
driver.get("https://the-internet.herokuapp.com/key_presses")
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys("afsefas") #отправляет введеные клавиши
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.CONTROL + "a") #отправляет одновременное нажатие клавиш
time.sleep(3)
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)
time.sleep(3)