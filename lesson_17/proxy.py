import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "username:password@45.159.250.127:8118" #текст для авторизации на прокси сервере. Цифры это ip и порт прокси сервера
# нихрена не загрузилось. Нкужно попробовать с платными или найти причину

options = Options()
options.add_argument(f"--proxy-server={PROXY_SERVER}")

driver = webdriver.Chrome(options=options)

driver.get("https://2ip.ru") #185.222.238.113

time.sleep(5)