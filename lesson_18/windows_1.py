import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# Локаторы
FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business '][1]")
START_FREE_BUTTON_LOCATOR = ("xpath", "(//div[text()='Start for Free'])[1]")

driver.get("https://hyperskill.org/courses")



#print(driver.current_window_handle) #дискриптор (уникальный идентификатор) текущей вкладки браузера
#print(driver.window_handles) #дискрипторы всех открытых вкладок

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
tabs = driver.window_handles
driver.switch_to.window(tabs[1]) #для одноразового переключения можно в скобках прописать driver.window_handles[1]
#webdriver не видит разницы между окном и вкладкой. Также переключается между всеми вкладками во всех окнах текущей сессии

driver.find_element(*START_FREE_BUTTON_LOCATOR).click()
time.sleep(3)

