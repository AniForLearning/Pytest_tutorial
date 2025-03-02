from locators.login_locators import login_page_locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username, timeout=5):
        self.enter_text(login_page_locators["username"], username, timeout)

    def enter_password(self, password, timeout=5):
        self.enter_text(login_page_locators["password"], password,timeout)

    def click_submit_button(self, timeout=5):
        self.click_element(login_page_locators["submit_button"], timeout)

    def login(self,username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button(timeout=5)