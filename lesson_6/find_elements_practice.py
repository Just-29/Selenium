import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://hyperskill.org/')
time.sleep(5)

driver.find_elements('class name', 'nav-link')[1].click()
time.sleep(3)