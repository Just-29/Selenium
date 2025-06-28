import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled") #отключение средства автоматизации браузера
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0") #представляемся user agent. Список есть в Инете

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

# driver.save_screenshot("screen.png") создает скриншот в директорию и дает название передающегося аргумента

driver.get("https://whatismyipaddress.com/")

wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))
