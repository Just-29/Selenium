import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

#print(driver.get_cookie("__ddg1_")) получение конкретного кука
#print(driver.get_cookies()) получение списка всех cookies

'''driver.add_cookie({ добавление кука
    "name": "gospod",
    "value": "Yahve"
})'''

'''before = driver.get_cookie("split") #сохраняем кук в переменную
print(before)
driver.delete_cookie("split") #удаляем кук
driver.add_cookie({ #добавляем свои  
    "name": "split",
    "value": "Yahve"
})
after = driver.get_cookie("split")
print(after)'''

before = driver.get_cookies()  #тоже самое для всех куков
print(before)
driver.delete_all_cookies()
driver.add_cookie({
    "name": "split",
    "value": "Yahve"
})
after = driver.get_cookies()
print("\n", after)