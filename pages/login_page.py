from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import Secrets


class LoginPage(BaseObject):

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CLASS_NAME, "login-button")
    ERROR_MSG = (By.CLASS_NAME, "error-message")
    LOGOUT_BTN = (By.CLASS_NAME, "logout-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self,
              username=Secrets.USER_NAME,
              password=Secrets.PASSWORD,):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_logout(self):
        self.click(self.LOGOUT_BTN)

    def get_error_msg(self):
        return self.get_text(self.ERROR_MSG)



