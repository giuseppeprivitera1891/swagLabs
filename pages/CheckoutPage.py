from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        print("CheckoutPage")
        self.page = page

        # locators
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_code = page.get_by_placeholder("Zip/Postal Code")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.continue_button = page.get_by_role("button", name="Continue")

        # variables
        self.first_name_text = "Andrew"
        self.last_name_text = "Brown"
        self.zip_code_text = "12345"
        self.cancel_button_text = "Cancel"
        self.continue_button_text = "Continue"





