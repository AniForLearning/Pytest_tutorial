import pytest

from locators.login_locators import Base_URL, Login_path
from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)

    login_page.open_url(Base_URL+Login_path)

    login_page.login("student","Password123")
    assert "logged-in-successfully" in driver.current_url

    login_page.take_screenshot("login_attempt_1.png")