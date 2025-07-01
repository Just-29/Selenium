import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.switch_to.new_window("tab") #открытие новой вкладки и переключение на нее. Написать window для открытия окна
input()