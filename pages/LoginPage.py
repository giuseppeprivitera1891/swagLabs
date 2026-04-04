from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

class LoginPage:
    def __init__(self, page: Page):
        print("LoginPage")
        self.page = page

        # locators
        self.username_textField = page.get_by_placeholder("Username")
        self.password_textField = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login_to_application(self, username, password):
        self.username_textField.fill(username)
        self.password_textField.fill(password)
        self.login_button.click()


