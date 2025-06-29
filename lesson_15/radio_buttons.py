import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/radio-button")

RADIO_BUTTON_YES_STATUS = ("xpath", "//input[@id='yesRadio']") #в радиокнопках input для проверки статуса
RADIO_BUTTON_NO_STATUS = ("xpath", "//input[@id='noRadio']") 
RADIO_BUTTON_YES_ACTIVE = ("xpath", "(//label[@class='custom-control-label'])[1]") #для взаимодействия нужно искать что-то рядом

print("\t", driver.find_element(*RADIO_BUTTON_YES_STATUS).is_selected()) #проверяем выбрана ли
driver.find_element(*RADIO_BUTTON_YES_ACTIVE).click()

print("\t", driver.find_element(*RADIO_BUTTON_YES_STATUS).is_selected()) 

print("\t", driver.find_element(*RADIO_BUTTON_NO_STATUS).is_enabled()) #проверяем доступна ли кнопка, так как не кликабельна