import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://cnt-450b0fcf-1da8-4b5c-b8cf-8af4f06fce39.containerhub.tripleten-services.com/")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the button using its XPath and click on it
driver.find_element(By.XPATH, "//button[@class='close-button input-close-button']").click()

# Pause execution for 2 seconds to allow you to see the results of the click
time.sleep(2)

# Close the browser and end the WebDriver session
driver.quit()