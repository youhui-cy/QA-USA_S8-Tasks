import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get("https://cnt-1ac96354-f52f-4a9c-bce3-272b05b171f6.containerhub.tripleten-services.com/")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the logo element using its CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")

# Print the found element to the console
print(element)

# Close the browser and end the WebDriver session
driver.quit()