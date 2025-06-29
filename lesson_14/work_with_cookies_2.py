import os
import pickle
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

'''LOGIN = ("xpath", "//input[@id='login_email']")
PASSWORD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

driver.find_element(*LOGIN).send_keys("haiman9255@gmail.com")
driver.find_element(*PASSWORD).send_keys("147896325")
driver.find_element(*SUBMIT_BUTTON).click()

pickle.dump(driver.get_cookies(), open(os.getcwd()+"\\cookies\\cookies.pkl", "wb"))'''

cookies = pickle.load(open(os.getcwd()+"\\cookies\\cookies.pkl", "rb"))

driver.delete_all_cookies()

for cooki in cookies:
    driver.add_cookie(cooki)

time.sleep(5)
driver.refresh()
time.sleep(5)