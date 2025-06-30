import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select #для работы с выпадающими списками

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

DROPDOWN_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
#DROPDOWN.select_by_visible_text("Option 1") вариант обращения по тексту
#DROPDOWN.select_by_value("1") вариант обращения по значению
#DROPDOWN.select_by_index(1) вариант обращения по номеру элемента. Отсчет с 0

all_options = DROPDOWN.options #выводит список всех вебэлементов опций

'''for option in all_options:
    time.sleep(1)
    if "Option 1" in option.text: для проверки наличия чего-нибудь в выпадающем списке
        print("Опция присутствует") 
    DROPDOWN.select_by_visible_text(option.text) перебирает все опции по тексту на них
'''
'''for option in all_options: 
    time.sleep(1)
    DROPDOWN.select_by_index(all_options.index(option)) перебирает все опции по их индексу
'''
for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value")) #перебирает по value