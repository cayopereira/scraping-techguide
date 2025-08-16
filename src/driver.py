from urllib.request import Request, urlopen, urlretrieve
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://techguide.sh/pt-BR/path/java/'
driver.get(url)
time.sleep(5)
buttons = driver.find_elements(By.TAG_NAME, 'button')

links = []
for button in buttons:
    try:
        button.click()
        links.append(driver.find_elements(By.TAG_NAME, 'a').get_attribute('href'))
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/svg').click()
        time.sleep(2)
    except:
        pass
print(len(links))

driver.quit()