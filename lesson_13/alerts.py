import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors") # Игнорировать ошибки сертификатов
options.add_argument("--allow-running-insecure-content") # Разрешить небезопасный контент

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
BUTTON_2 = ("xpath", "//button[@id='timerAlertButton']")
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
BUTTON_4 = ("xpath", "//button[@id='promtButton']")

wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present()) # когда появится алерт, запишется сюда

driver.switch_to.alert #переключение на алерт
time.sleep(3)
print(alert.text)
#alert.accept() принимаем алерт
#alert.dismiss()  отклоняет алерт
alert.send_keys("Holy Shit!!!")
alert.accept()
time.sleep(3)