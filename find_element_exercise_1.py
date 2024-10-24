import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the title element using its CSS Selector
driver...

# Close the browser and end the WebDriver session
driver...
