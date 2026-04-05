from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class LoginPage:
    def __init__(self, page: Page):
        print("LoginPage")
        self.page = page

        # locators
        self.username_textField = page.get_by_placeholder("Username")
        self.password_textField = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.product_label = page.locator("span[class='title'")

        # variables
        self.product_label_text = "Products"

    def login_to_application(self, username, password):
        self.username_textField.fill(username)
        self.password_textField.fill(password)
        self.login_button.click()

    def check_login_access(self):
        # checks if the access is correct
        expect(self.product_label).to_have_text(self.product_label_text)
        get_product_text = self.product_label.text_content()
        print(f"The product label text is {get_product_text}")

