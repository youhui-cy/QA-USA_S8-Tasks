import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://cnt-ba9b2ec5-70eb-47dd-9040-79fc0572b7c4.containerhub.tripleten-services.com/")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find all elements on the page using an XPath selector
elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

# Check that the number of elements found is greater than 1 by using len()
assert len(elements) > 1

# Close the browser and end the WebDriver session
driver.quit
