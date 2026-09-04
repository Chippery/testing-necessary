from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://us-2.fountain.com/apply/ups/applications/33b1b04f-bbb0-4582-bfa4-f107179b5a83")

time.sleep(5)

text_to_find = "We're sorry - the opportunity you were applying for has been filled! You can navigate back to the careers page to look for other opportunities."
# Finds any element containing "Welcome"
element = driver.find_element(By.XPATH, "//*[contains(text()='sorry')]")

print(element)

time.sleep(5)

driver.quit()