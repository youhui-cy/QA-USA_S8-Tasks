import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the "Sign up" button using its XPath and click on it
driver.find_element(...)...

# Pause execution for 2 seconds to allow you to see the results of the click
time.sleep(2)

# Close the browser and end the WebDriver session
driver.quit()
