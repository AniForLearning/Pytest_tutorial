from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_open_browser(driver):
    driver.get('https://practicetestautomation.com/practice-test-login/')
    username = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
    password = driver.find_element(by=By.ID, value='password')
    username.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
    password.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "password")))

def test_valid_login(driver):
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.find_element(by=By.ID, value='username').send_keys('student')
    driver.find_element(by=By.ID, value='password').send_keys('Password123')
    driver.find_element(by=By.ID, value='submit').click()
    WebDriverWait(driver, 5).until(EC.url_contains("logged-in-successfully"))
    assert "logged-in-successfully" in driver.current_url

def test_invalid_username(driver):
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.find_element(by=By.ID, value='username').send_keys('not student')
    driver.find_element(by=By.ID, value='password').send_keys('Password123')
    driver.find_element(by=By.ID, value='submit').click()
    error = driver.find_element(by=By.ID, value='error').text
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'error')))
    assert "Your username is invalid!" in error

def test_invalid_password(driver):
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.find_element(by=By.ID, value='username').send_keys('student')
    driver.find_element(by=By.ID, value='password').send_keys('notPassword123')
    driver.find_element(by=By.ID, value='submit').click()
    error = driver.find_element(by=By.ID, value='error').text
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'error')))
    assert "Your password is invalid!" in error

def test_empty_fields(driver):
    driver.get('https://practicetestautomation.com/practice-test-login/')
    driver.find_element(by=By.ID, value='submit').click()
    error = driver.find_element(by=By.ID, value='error').text
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'error')))
    assert "Your username is invalid!" in error
