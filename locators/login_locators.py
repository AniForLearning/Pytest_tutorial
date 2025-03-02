Login_path = 'practice-test-login/'
Base_URL = 'https://practicetestautomation.com/'

from selenium.webdriver.common.by import By

login_page_locators = {
    "username": (By.ID, 'username'),
    "password": (By.ID, 'password'),
    "submit_button": (By.XPATH, "//*[@id='submit']")
}
