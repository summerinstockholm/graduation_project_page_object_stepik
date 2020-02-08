from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_MAIL = (By.XPATH, "//input[@name='login-username']")
    LOGIN_PASS = (By.XPATH, "//input[@name='login-password']")
    REG_MAIL = (By.XPATH, "//input[@name='registration-email']")
    REG_PASS = (By.XPATH, "//input[@name='registration-password1']")
