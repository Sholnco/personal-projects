from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace with your login details and target site
username = "your_username"
password = "your_password"
post_message = "This is my new post!"  # The message you want to post

# Start Chrome browser
driver = webdriver.Chrome()  # Ensure chromedriver is in the same folder or PATH

# Open the login page
driver.get("https://facebook.com/login")  # Replace with the actual login page

# Wait for page to load
time.sleep(2)

# Fill in username and password (use the correct element IDs or names)
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# Click login button
driver.find_element(By.ID, "login").click()

# Wait for login to complete
time.sleep(5)

# After logging in, find the text box or text area for the post (example: 'post-box')
post_box = driver.find_element(By.ID, "post-box")  # Replace with actual ID, name, or class of the post box
post_box.send_keys(post_message)  # Type your post message

# Now click the post button (example: 'submit-post')
submit_button = driver.find_element(By.ID, "submit-post")  # Replace with actual button ID
submit_button.click()  # This submits your post

# Wait a few seconds to ensure the post is made
time.sleep(5)

# Close the browser
driver.quit()
