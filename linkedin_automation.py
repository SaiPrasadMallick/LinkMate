from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from config import linkedin_username, linkedin_password

class LinkedInAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome('C:\\Program Files\\Web Driver\\chromedriver.exe')

    def login(self, username, password):
        # Go to LinkedIn login page
        self.driver.get("https://www.linkedin.com/login")

        # Fill in the username and password fields
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.ENTER)
        time.sleep(3)  # Add a delay for the page to load

    def send_connection_requests(self):
        # Go to "My Network" page
        self.driver.get("https://www.linkedin.com/mynetwork")

        time.sleep(5)  # Add a delay for the page to load

        # Find and click the 'Connect' button to send a request to potential connections
        connect_buttons = self.driver.find_elements_by_css_selector(".invitation-card__action-btn")
        for button in connect_buttons:
            button.click()
            time.sleep(1)  # Add a delay for the request to be sent

    def __del__(self):
        self.driver.quit()
