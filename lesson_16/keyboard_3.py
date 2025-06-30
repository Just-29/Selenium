import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")

driver.find_element(*MULTISELECT_LOCATOR).send_keys("Green")
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
driver.find_element(*MULTISELECT_LOCATOR).send_keys("Black")
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)