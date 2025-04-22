from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get("https://cnt-91d5be95-9f46-4965-9f71-d3dd9add9dfa.containerhub.tripleten-services.com/")

time.sleep(2)

# Gets the element's text
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Assert that the text of the disclaimer variable is "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()