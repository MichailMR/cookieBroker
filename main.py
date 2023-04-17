import requests
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://orteil.dashnet.org/cookieclicker"
print("\nvisit:", url)

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--ignore-certificate-errors')
#options.add_argument("--headless")
#options.add_argument("--log-level=3")

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.maximize_window()

###Get to cookie clicker
time.sleep(1)
driver.find_element("xpath", "//p[@class='fc-button-label']").click()

time.sleep(1)
driver.find_element("xpath", "//*[@id='langSelect-EN']").click()

###Import stock account
time.sleep(6)
driver.execute_script('Game.ImportSave()')

time.sleep(1)
export = open("export.txt", "r").read()

time.sleep(1)
driver.find_element("xpath", "//*[@id='textareaPrompt']").send_keys(export)

time.sleep(1)
driver.find_element("xpath", "//*[@id='promptOption0']").click()

script = '''
var c = document.getElementById("bankStocks");
'''

test = driver.execute_script(script)

time.sleep(100)
driver.quit()

"""
driver.find_element(By.CLASS_NAME,"Consent").click()
time.sleep(1)

driver.find_element(By.XPATH, "//a[@lang='"+languageTo+"']").click()
time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")
translation = soup.find(id='firstHeading').get_text()
    
print("\n", translation)
"""