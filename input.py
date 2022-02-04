from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = 'https://www.mercadolibre.com.ar/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

buscar = driver.find_elements(By.XPATH,'//input[@class="nav-search-input"]')
buscar.click()
time.sleep(2)
buscar.send_keys('Televisor plasma')