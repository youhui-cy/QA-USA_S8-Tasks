import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-450b0fcf-1da8-4b5c-b8cf-8af4f06fce39.containerhub.tripleten-services.com/")

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()