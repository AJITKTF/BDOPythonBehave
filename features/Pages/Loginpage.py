import time

from selenium.webdriver.common.by import By

from features.Pages.Basepage import Basepage


class LoginPage(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    enter_username = "username"
    enter_password = "password"
    click_signin = "login"
    login_successful_xpath = "//div[contains(text(),'Login Successful')]"
    continue_button_xpath = "//span[contains(text(),'Continue')]"
    logout_button_xpath = "//a[contains(text(),' Logout ')]"

    def enter_username_textbox(self, username):
        self.send_text("id", self.enter_username, username)

    def enter_password_textbox(self, password):
        self.send_text("id", self.enter_password, password)

    def click_on_signin(self):
        self.click_element("name",self.click_signin)

    def validate_login_successful(self):
        self.wait_method()
        return self.display_element("xpath", self.login_successful_xpath)

    def click_continue_button(self):
        self.click_element("xpath", self.continue_button_xpath)

    def click_logout_button(self):
        self.click_element("xpath",self.logout_button_xpath)
