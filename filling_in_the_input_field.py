import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver...

# Find the TO field and fill it in
driver...

time.sleep(2)

# Find the "Call a taxi" button and click on it
driver...

# Add an explicit wait for the field to load
WebDriverWait(...).until(...)

# Write a comment to the driver
driver...

time.sleep(2)

# Check that your comment is what you expect it to be
assert ...

driver.quit()
