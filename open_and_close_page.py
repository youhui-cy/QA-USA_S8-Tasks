from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the test stand page
driver.get('https://www.google.com/imghp')

# Check that /signin was added to the URL
assert '/imghp' in driver.current_url

# Close the browser
driver.quit()