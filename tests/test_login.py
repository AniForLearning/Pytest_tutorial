import pytest

from locators.login_locators import Base_URL, Login_path, login_page_locators
from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_url(Base_URL+Login_path)
    login_page.login("student","Password123")
    assert "logged-in-successfully" in driver.current_url

    login_page.take_screenshot("login_attempt_1.png")

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open_url(Base_URL + Login_path)
    login_page.login("not student", "Password123")
    error = login_page.find_element(login_page_locators["error"]).text
    assert "Your username is invalid!" in error

    login_page.take_screenshot("login_attempt_2.png")


def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open_url(Base_URL + Login_path)
    login_page.login("student", "notPassword123")
    error = login_page.find_element(login_page_locators["error"]).text
    assert "Your password is invalid!" in error

    login_page.take_screenshot("login_attempt_3.png")

def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open_url(Base_URL + Login_path)
    login_page.login("", "")
    error = login_page.find_element(login_page_locators["error"]).text
    assert "Your username is invalid!" in error

    login_page.take_screenshot("login_attempt_4.png")

