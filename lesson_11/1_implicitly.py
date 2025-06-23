from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.implicitly_wait(10) #активация неявного ожидания в 10 сек

driver.get('https://demoqa.com/dynamic-properties')
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']") #создаем кортеж с необходимыми данными для поиска xpath

driver.find_element(*VISIBLE_AFTER_BUTTON).click() #распаковываем кортеж и передаем в поиск элемента