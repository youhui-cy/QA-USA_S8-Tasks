from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get ("https://cnt-e53f07f0-4085-4eb8-b4b6-584822cf7ce3.containerhub.tripleten-services.com/")

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url

# Close the browser
driver.quit()
