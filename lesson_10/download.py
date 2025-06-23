import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
script_dir = os.path.dirname(os.path.abspath(__file__))
downloads_dir = os.path.join(script_dir, "downloads")
prefs = { #prefs или preferens это специфичные настройки браузера
    "download.default_directory": downloads_dir 
} # r перед f строкой избавляет от сообщения об ошибке. Сырая строка чтоб не экранировал
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)

driver.find_elements("xpath", "(//a)")[10].click()
time.sleep(3)