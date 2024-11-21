import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver...

# Find the TO field and fill it in
driver...

time.sleep(2)

# Get the text from "Fastest" mode
mode = ...

time.sleep(2)

# Assert that the text of the mode variable is "Fastest"
assert ...

driver.quit()
