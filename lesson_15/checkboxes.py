import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")

#CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")

#print(driver.find_element(*CHECKBOX_1).get_attribute("checked")) #делаем запрос на наличие вписанной строки в элементе. Возвращает либо None, либо строку "true"
#print(driver.find_element(*CHECKBOX_1).is_selected()) #тоже самое встроенным методом
#driver.find_element(*CHECKBOX_1).click()

#assert driver.find_element(*CHECKBOX_1).get_attribute("checked") == "true" #пример проверки на наличие галочки в чекбоксе
#print(driver.find_element(*CHECKBOX_1).is_selected()) #возвращает булевые True, False

'''CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']") #находим сам input для определения статуса
CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']") #кликаем на другой элемент в чекбоксе для взаимодействия
print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
driver.find_element(*CHECKBOX_HOME_ACTION).click()
print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())'''

ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")
before = driver.find_element(*ELEMENT_ONE).get_attribute("class") #если нет "checked", ищем "active" или любые другие изменения после нажатия
print(before)
driver.find_element(*ELEMENT_ONE).click()
after = driver.find_element(*ELEMENT_ONE).get_attribute("class")
if  "active" in after: # после клика задаем проверку на наличие слова подтверждающегонажатие
    print("Элемент активен")
else:
    print("Элемент не активен")