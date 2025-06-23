import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
#chrome_options.page_load_strategy = "eager" выбор прогрузки чтраницы normal или eager
#chrome_options.add_argument("--headless") запуск в фоновом режиме
#chrome_options.add_argument("--incognito") запуск в режиме инкогнито
#chrome_options.add_argument("--ignore-certificate-errors") запуск с игнорированием ошибок сертификата страницы
#chrome_options.add_argument("--window-size=300,300") размер окна 
#chrome_options.add_argument("--disable-cache") отключение кеширования
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()
#driver.maximize_window() поставить максимальный размер окна браузера
#driver.set_window_size(700, 700) установить размер окна браузера после его вызова

driver.get("https://whatismyipaddress.com/")

end_time = time.time()
result = end_time - start_time
print(result)
time.sleep(3)