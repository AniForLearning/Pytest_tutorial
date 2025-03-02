import os.path

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from conftest import driver
from locators.login_locators import Base_URL, Login_path

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def enter_text(self, locator, text, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()  # Clears any existing text
        element.send_keys(text)

    def click_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def take_screenshot(self,filename= "screenshot.png"):
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir,filename)

        self.driver.get_screenshot_as_file(screenshot_path)

        with open(screenshot_path, "rb") as file:
            allure.attach(file.read(), name=filename, attachment_type=allure.attachment_type.PNG)

        print(f"Screenshot saved to {screenshot_path}")