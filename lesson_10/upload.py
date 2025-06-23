import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)

#file_path = os.path.abspath(__file__) путь до текущего файла
script_dir = os.path.dirname(os.path.abspath(__file__)) #определяем путь к директории скрипта через путь к текущему файлу
file_path = os.path.join(script_dir, "downloads", "китай.jpg") #определяем путь к файлу прописав путь от директории скрипта к нужному файлу
driver.find_element("xpath", "//input[@id='file-upload']").send_keys(file_path)
time.sleep(6)

'''Если загрузка скрыта за button, значит нужно найти скрытый //input[@type="file"]'''