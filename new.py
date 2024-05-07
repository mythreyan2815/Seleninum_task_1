from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

linkedin_username = 'mythreyan2805@gmail.com'
linkedin_password = 'Mythreyan@28'

chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# Create ChromeOptions object and set binary location
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Create a new instance of the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Wait for the page to load (you might need to adjust the time depending on your internet speed)
time.sleep(2)

# Find the username and password input fields and input your credentials
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(linkedin_username)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(linkedin_password)

# Simulate pressing Enter to submit the login form
password_field.send_keys(Keys.ENTER)

# Wait for the login to complete (you might need to adjust the time depending on your internet speed)
time.sleep(5)

# Navigate to the search bar and enter the search query
search_query = "software companies in chennai"
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_bar.send_keys(search_query)
search_bar.send_keys(Keys.ENTER)

# Wait for the search results to load (you might need to adjust the time depending on your internet speed)
time.sleep(5)

# Now you can perform actions on the search results page

# Close the browser window when done
driver.quit()
